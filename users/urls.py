from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from users import views

urlpatterns = [
    path('register/', views.signup, name="register"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate')
]
