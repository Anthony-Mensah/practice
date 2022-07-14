from . import views
from django.urls import path

urlpatterns = [
	path('', views.home,name='home'),
	path('signup', views.signup,name='signup'),
	path('login', views.login,name='login'),
	path('logout', views.logout,name='logout'),
	path('displayItem/<str:pk>', views.displayItem,name='displayItem'),
	path('displayItem/signup', views.signup,name='signup'),
]