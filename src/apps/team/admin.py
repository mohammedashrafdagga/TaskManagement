from django.contrib import admin
from .models import Team
# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    # readonly_fields = ['__all__']
    list_display = ['leader', 'title', 'code', 'create_at']

    def get_readonly_fields(self, request, obj):
        return [f.name for f in self.model._meta.fields]
