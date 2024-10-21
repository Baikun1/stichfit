from django.urls import path
from user.views import*
app_name='user'
urlpatterns = [
    path('',profile,name='profile'),
    path('signin/', signin, name='signin'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]