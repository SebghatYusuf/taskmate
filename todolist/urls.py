from django.urls import include, path
from .views import *

urlpatterns = [
    path('', todolist, name="todo-list"),
    path('delete/<int:task_id>/', delete_task, name="delete-task"),
    path('edit/<int:task_id>/', edit_task, name="edit-task"),
    path('complete/<int:task_id>/', complete_task, name="complete-task"),
    path('pending/<int:task_id>/', pending_task, name="pending-task"),
]