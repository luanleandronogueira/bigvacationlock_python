from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('homes/', views.houses, name='houses'),
    path('create_house/', views.create_house, name='create_house'),
    path('insert_house', views.insert_house, name='insert_house')

    
]