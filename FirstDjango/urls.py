from django.urls import path
from MainApp import views


urlpatterns = [
    path('', views.home ),
    path('about/', views.about),
    path('item/', views.get_item)
]

