from django.conf.urls import patterns, url
from . import views 
urlpatterns = patterns(
	'question.views',
    url(r'^add/$', views.question_add, name='question_add'),
    url(r'^$', views.question_list, name='question_list'),
    url(r'^categories/$', views.category_list, name='category_list'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.question_detail, name='question_detail'),
	url(r'^category/(?P<category>.+)/$', views.question_category_list, name='question_category_list'),
)