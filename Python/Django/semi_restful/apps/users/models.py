from django.db import models

# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!! 
# (just parts, like request.POST)
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 0:
            errors["name"] = "First name cannot be blank"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


