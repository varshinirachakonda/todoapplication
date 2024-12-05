from django.contrib import admin

# Register your models here.
from app.models import Task
class Taskadmin(admin.ModelAdmin):
    list_display=('task','is_completed')
    search_fields=('task',)
admin.site.register(Task,Taskadmin)