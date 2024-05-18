from django.urls import path
from . import views


urlpatterns = [
    path('', views.login , name='user_login'),
    path('register', views.register, name='register' ),
    path('logout', views.logout, name='user_logout' )
    
]
