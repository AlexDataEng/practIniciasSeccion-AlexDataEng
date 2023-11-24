from django.urls import path
from .views import login, homeInforme
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", login),
    path("home/", homeInforme, name="inicio-informe"),
    #path("iniciar/", iniciarSesion, name="iniciarSesion"),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', your_signup_view, name='signup'),
    
]
