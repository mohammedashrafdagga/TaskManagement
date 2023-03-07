from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activate_token
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Account
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# register page
def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm()
    if request.method == 'POST':
        # collection information
        form = RegisterForm(request.POST)
        # if valid the form
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # now send a email
            current_site = get_current_site(request)
            subject = 'Active your account'
            message = render_to_string(
                'account/components/account_activate_email.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activate_token.make_token(user)
                })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered successful and activation sent')
    return render(request, 'account/register.html', {'form': form})


# now activate
def activate_user(request, uidb64, token) -> None:
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
        if user and account_activate_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return render(request, 'account/components/activate_valid.html')
        else:
            return render(request, 'account/components/activate_invalid.html')
    except:
        return render(request, 'account/components/activate_invalid.html', {'error': 'invalid activate'})


@login_required
def change_password(request):
    '''
        Allow User update Password
    '''
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('team:team-main')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})
