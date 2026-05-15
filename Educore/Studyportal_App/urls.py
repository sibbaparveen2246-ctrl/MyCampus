from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.user_signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('add/', views.add_student, name='add'),
    path('search/', views.search_student, name='search'),
    path('update/', views.update_student, name='update'),
    path('delete/', views.delete_student, name='delete'),
]
