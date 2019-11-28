from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^$', views.search_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.search_detail, name="detail"),
]
