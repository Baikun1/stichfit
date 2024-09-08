from django.urls import path
from service.views import*
# APP_NAME='service'
app_name='service'
urlpatterns = [
    path('',service,name='home'),
    path('custom',custom,name='custom'),
    path('alternation',alternation,name='alternation'),
    path('favric',favric,name='favric'),
    path('consltant',consultant,name='consultant'),


]
