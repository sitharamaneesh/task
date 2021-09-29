from django.urls import path
from .import views
from task import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('validation',views.validation,name='validation'),
    path('validatelogin',views.validlogin,name='validatelogin'),
    path('userview',views.userdetail,name='userview'),
    path('alter',views.alter,name='alter'),
    path('logoutuser',views.logoutview,name='logoutuser'),
    
]+static(settings.STATIC_URL)