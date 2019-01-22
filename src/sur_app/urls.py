from django.urls import path

from . import views

urlpatterns = [
    path('sex_destribution', views.sex_destribution, name='sex_destribution'),
    path('relation_destribution', views.relation_destribution, name='relation_destribution'),
    path('raw_data', views.raw_data, name='raw_data'),
]
