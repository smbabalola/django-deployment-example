from django.conf.urls import url
from basictemp_app import views

#Template tagging
app_name = 'basictemp_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
