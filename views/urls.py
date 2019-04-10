from django.conf.urls import  url

from views import views

urlpatterns = [
	# Welcome Page
	url(r'^$', views.base_Page),
]
