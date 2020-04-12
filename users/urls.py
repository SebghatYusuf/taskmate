from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from users import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
]
