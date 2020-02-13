from django.conf.urls import url

from . import views

app_name = 'graphing'
urlpatterns = [
    url(r'^showgraph/$', views.graph_file, name='showgraph'),
    url(r'^$', views.selection, name='selection'),
    url(r'^selectfile/$', views.select_file, name='select_file'),
]