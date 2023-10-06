from django.contrib import admin
from .models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    model = Robot
    list_display = ['model', 'version', 'created']
