from django.conf.urls import url
from . import views


urlpatterns = [

    #sets the url link to homepage
    url('^$', views.HomeView.as_view(), name="home"),

    #sets the url pattern to a detail page of a staff using the id and name
    url('^(?P<pk>[0-9]+)/(?P<name>.+)/', views.StaffView.as_view(), name="staff"),
    url('transfer/<int:pk>', views.TransfersView.as_view(), name="staff"),
]