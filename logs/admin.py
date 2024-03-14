from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Logs, Progress

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(Logs)
class Logs (admin.ModelAdmin):
    list_display= [
        "user",
        "log_id",
        "time_of_serving",
    ]

@admin.register(Progress)
class Progress (admin.ModelAdmin):
    list_display= [
        "user",
        "progress_id",
        "fiber_actual",
        "fat_actual",
        "date"
    ]
