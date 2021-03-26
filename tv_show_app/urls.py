from django.urls import path   
from . import views

urlpatterns = [
    path('', views.log_and_reg), #This is the initial page and also displays after clicking Delete button
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    #path('login', views.login),
    path('shows', views.shows),#This displays after clicking the GO BACK link 
    path('shows/<int:id>', views.get_show), #This applies when hitting the Show link on the main page
    path('shows/<int:id>/delete', views.delete), #This applies when hitting Delete button on the main page
    path('shows/new', views.new_show), #This applies when hitting Add a New Show link on the main page
    path('shows/create', views.create), #This applies when hitting create button on the Add a New Show page
    path('shows/<int:id>/edit', views.show_edit), #This applies when hitting edit button on the main page
    path('shows/<int:id>/update', views.update),  #This applies when hitting submit button on the edit page
]           