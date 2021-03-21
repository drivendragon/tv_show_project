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