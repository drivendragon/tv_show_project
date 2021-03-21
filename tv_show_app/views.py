from django.shortcuts import render, HttpResponse, redirect
from .models import Shows
from django.contrib import messages


def shows(request):
  context = {
    "shows": Shows.objects.all()
  }
  return render(request, "index.html", context)


def get_show(request, id):
  context = {
    "shows": Shows.objects.get(id=id)
  }
  return render(request, "show.html", context)

def new_show(request):
  return render(request, "new_show.html")

#def create(request):
#  if request.method == "POST":
##    newly_created_show = Shows(title=request.POST['title'], network=request.POST['network'], description=request.POST['description'], releaseDate=request.POST['releaseDate'])
#    newly_created_show.save()
#    return redirect(f"/shows/{newly_created_show.id}")
#  return redirect("/shows")

def create(request):
  if request.method == "POST":
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
      # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
      for key, value in errors.items():
        messages.error(request, value) 
        return redirect("/shows/new")      
    newly_created_show = Shows(title=request.POST['title'], network=request.POST['network'], description=request.POST['description'], releaseDate=request.POST['releaseDate'])
    newly_created_show.save()
    return redirect(f"/shows/{newly_created_show.id}")
  return redirect("/shows")

def delete(request,id):
  if request.method =="POST":
    shows = Shows.objects.get(id=id)
    shows.delete()
  return redirect("/")

def show_edit(request,id):
  context = {
    "shows": Shows.objects.get(id=id)
    }
  return render(request, "edit_show.html", context)

def update(request,id):
  if request.method=="POST":
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
      # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
      for key, value in errors.items():
        messages.error(request, value) 
        return redirect(f"/shows/{id}/edit")      
    else:
      # if the errors object is empty, that means there were no errors!
      # retrieve the blog to be updated, make the changes, and save
      shows = Shows.objects.get(id=id)
      shows.title = request.POST['title']
      shows.network = request.POST['network']
      shows.releaseDate = request.POST['releaseDate']
      shows.description = request.POST['description']
      shows.save()
      messages.success(request, "Show successfully updated")
  return redirect(f"/shows/{id}")
      
  

