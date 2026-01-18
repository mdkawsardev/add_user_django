from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userlogin, name='userlogin'),
    path('register/', views.userregister, name='userregister'),
    path('logout/', views.userlogout, name='userlogout'),
    path('post/<int:pk>/', views.post, name='post'),
]
