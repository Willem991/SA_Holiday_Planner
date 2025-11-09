from django.urls import path
from django.contrib.auth import views as authviews

app_name = 'accounts'

urlpatterns = [
    path('login/', authviews.LoginView.as_view(template_name='accounts/login.html'), name='login')
]
