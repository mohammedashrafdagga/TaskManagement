from django.contrib import admin
from .models import Account


# adding Account Model into admin site
admin.site.register(Account)
