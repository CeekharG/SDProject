from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('register', views.register),
    path('create_profile', views.user_profile),
    path('quote', views.fuel_quote),
<<<<<<< HEAD
    path('history', views.fuel_quote_history)
=======
    path('history', views.fuel_quote_history),
    path('logout', views.logout)
>>>>>>> BugFix
]
