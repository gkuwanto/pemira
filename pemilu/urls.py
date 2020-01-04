from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote', views.vote, name='vote'),
    path('count', views.quick_count, name='count')
]
