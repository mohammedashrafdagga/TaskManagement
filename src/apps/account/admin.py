from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.

# unregister
admin.site.unregister(User)
admin.site.unregister(Group)


# override that
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'pk']


# register User Model
admin.site.register(User, UserAdmin)
