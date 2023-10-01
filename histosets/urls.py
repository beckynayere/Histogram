from . import views
from django.urls import path, include, re_path  

urlpatterns = [
    path('insertSamples/', views.insert_samples, name='insert_samples'),
   re_path(r'^metrics/$', views.get_metrics, name='get_metrics'),
]