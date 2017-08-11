from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.schedule_chart, name='schedule_chart'),
    url(r'^table/', views.schedule_table, name='schedule_table')
]