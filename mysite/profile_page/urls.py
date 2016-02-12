from django.conf.urls import url
from . import views

urlpatterns = [
	# ex: /profile/
	url(r'^$', views.index, name='index'),
	# ex: /profile/1/
	url(r'^(?P<id>\d+)/$', views.published, name='published'),
]