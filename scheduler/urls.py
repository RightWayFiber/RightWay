from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.chart, name='chart'),
    url(r'^chart/', views.chart, name='chart'),
    url(r'^table/', views.table, name='table')
]