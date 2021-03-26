from django.shortcuts import render, HttpResponse, redirect
from .models import Shows, User
from django.contrib import messages
import bcrypt

def log_and_reg(request):
  return render(request, "log_and_reg.html")

def register(request):
  if request.method == "POST":
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
    else:
      password = request.POST['password']
      pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
      user = User.objects.create(username=request.POST['username'], password=pw_hash)
      request.session['user_id'] = user.id
      return redirect("/shows")
  return redirect("/")

def login(request):
  if request.method == "POST":
      user = User.objects.filter(username=request.POST['username'])
      if user: 
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
          request.session['user_id'] = logged_user.id
          messages.success(request, "Successfully logged in")
          return redirect("/shows")
        messages.error(request, "Password does not match")
      else:
        messages.error(request, "Username does not exist")

  return redirect("/")


def logout(request):
  request.session.flush()
  return redirect("/")

def shows(request):
  if not 'user_id' in request.session:
    return redirect("/")
  context = {
    "shows": Shows.objects.all(),
    "user": User.objects.get(id=request.session['user_id'])
  }
  return render(request, "index.html", context)


def get_show(request, id):
  context = {
    "shows": Shows.objects.get(id=id)
  }
  return render(request, "show.html", context)

def new_show(request): #applies when hitting Add a New Show link on the main page
  return render(request, "new_show.html")

def create(request):   #applies at CREATE button on the Add Show Page
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

def delete(request,id):  #applies when hitting Delete button on the main page
  if request.method =="POST":
    shows = Shows.objects.get(id=id)
    shows.delete()
  return redirect("/")

def show_edit(request,id):  #applies when hitting edit button on the main page
  context = {
    "shows": Shows.objects.get(id=id)
    }
  return render(request, "edit_show.html", context)

def update(request,id): #applies when hitting submit button on the edit page
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
      
  

