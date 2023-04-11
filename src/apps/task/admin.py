from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['team', 'title', 'slug', 'due_date']

    def get_readonly_fields(self, request, obj):
        return [f.name for f in self.model._meta.fields]
