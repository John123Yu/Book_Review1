from django.conf.urls import url, include # Notice we added include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users$', views.register),
	url(r'^login$', views.login),
	url(r'^success$', views.success)
	]
# 	url(r'^emails$', views.create),
# 	url(r'^success$', views.success),
# 	url(r'^emails/(?P<id>[0-9]*)/delete', views.destroy)
# ]