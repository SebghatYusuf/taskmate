
from django.contrib import admin
from django.urls import path, include
from todolist import views as todo_list_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list_views.index, name='index'),
    path('tasklist/', include('todolist.urls')),
    path('account/', include('users.urls')),
    path('about/', todo_list_views.about, name="about"),
    path('contact/', todo_list_views.contact, name="contact"),
]
