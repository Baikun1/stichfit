"""
URL configuration for tailor project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from home.views import*
app_name='home'
urlpatterns = [
    path('',home,name='home'),

    path('about-us/', about_us, name='about_us'),
    path('careers/', careers, name='careers'),
    path('press/', press, name='press'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('help-center/', help_center, name='help_center'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
    path('faq/', faq, name='faq'),
    path('feedback/', feedback, name='feedback'),
    path('documentation/', documentation, name='documentation'),
    path('api-reference/', api_reference, name='api_reference'),
    path('guides/', guides, name='guides'),
    path('community/', community, name='community'),
    path('events/', events, name='events'),
    
]
