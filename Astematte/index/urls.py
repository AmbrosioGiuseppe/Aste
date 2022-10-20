from django.urls import path
from . import views
from .views import *

app_name = 'index'

urlpatterns = [
	#path('profile/', views.profile, name='profile'),
	path('', views.index, name='index'),
]