from django.urls import path
from . import views
from .views import *

app_name = 'accounts'

urlpatterns = [
	#re_path(r'^profile/$',views.profile,name='profile'),
	path('profile/', views.profile, name='profile'),
]