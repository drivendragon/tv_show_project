from django.urls import path   
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/<int:id>', views.get_show),
    path('shows/<int:id>/delete', views.delete),
    path('shows/new', views.new_show),
    path('shows/create', views.create),
    path('shows/<int:id>/edit', views.show_edit),
    path('shows/<int:id>/update', views.update),
]