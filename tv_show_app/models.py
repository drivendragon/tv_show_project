from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 6:
            errors["name"] = "Title should be at least 5 characters"
        if len(postData['network']) < 2:
            errors["desc"] = "Network should be at least 3 characters"
        if len(postData['description']) < 11:
            errors["desc"] = "Description should be at least 10 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    
class UserManager(models.Manager):
    def register_validator(self, postData):    
        errors = {}
        if len(postData['username']) < 2:
            errors['username'] = "Username must be at least 2 characters"
        if len(postData['password']) < 8:
            errors['username'] = "Password must be at least 8 characters"
        if not postData['password'] == postData['confirm_password']:
            errors['confirm_pw'] = "Passwords must match"
        return errors

class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

        #EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
        #    errors['email'] = ("Invalid email address!")
        #return errors