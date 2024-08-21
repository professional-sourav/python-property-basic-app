from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_view, name='listing'),
    path('add-new/', views.add_new, name='add_new')
]
