from django.contrib import admin
from todolist.models import *


class TodoListAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskList
        diplay_list = ('task', 'done')


admin.site.register(TaskList, TodoListAdmin)
