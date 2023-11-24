from django.urls import path
from .views import login, homeInforme, home, logout_view
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", login, name="iniciarSesion"),
    path("inicio-informe/", login_required(homeInforme), name="inicio-informe"),
    path("inicio/", home, name="inicio"),
    path("", logout_view, name="logout_view")
    


    #path("iniciar/", iniciarSesion, name="iniciarSesion"),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', your_signup_view, name='signup'),
    
]
