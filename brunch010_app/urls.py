from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^$', views.post_home, name='post_home'),								#Post Homepage
	url(r'^create/$', views.post_create, name='post_create'),					#Post Create
	url(r'^posts/(?P<id>\d+)$', views.post_detail, name='post_detail'),			#Post Detail
	url(r'^posts/(?P<id>\d+)/edit/$', views.post_update, name='post_update'),	#Post Update
	url(r'^delete/$', views.post_delete, name='post_delete'),					#Post Delete
]