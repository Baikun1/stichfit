from django.urls import path
from user.views import*
app_name='user'
urlpatterns = [
    path('',profile,name='profile'),
    path('signin/', signin, name='signin'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]