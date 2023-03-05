from django.shortcuts import render


# Home page view in core project
def home_page(request):
    return render(request, 'home.html')
