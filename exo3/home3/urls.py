from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('singleblog', views.singleblog, name='singleblog'),
    path('event', views.event, name='event'),
    path('eventdetails', views.eventdetails, name='eventdetails'),
    path('elements', views.elements, name='elements'),
    path('courses', views.courses, name='courses'),
    path('admission', views.admission, name='admission')




]