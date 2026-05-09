from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add'),
    path('search/', views.search_student, name='search'),
    path('update/', views.update_student, name='update'),
    path('delete/', views.delete_student, name='delete'),
]
