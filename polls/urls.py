from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^user/register/$', views.user_register, name='register'),
	url(r'^user/login/$', views.user_login, name='login'),
	url(r'^user/logout/$', views.user_logout, name='logout'),
	url(r'^user/profile/$', views.user_profile, name='profile'),
]

handler404 = 'polls.views.custom_404'