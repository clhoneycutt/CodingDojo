from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!! 
# (just parts, like request.POST)
class UserManager(models.Manager):
    def check_duplicates(self, email):
        pass

    def validate(self, postData):
        errors = {}
        
        # First name validations============
        if len(postData['first_name']) < 0:
            errors["first_name"] = "First name cannot be blank"
        elif len(postData["first_name"]) > 60:
            errors["first_name"] = "First name cannot be longer than 60 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors["first_name"] = "First name must contain at least two letters and only contain letters."
        return errors

        # ==================================

        # Last name validations=============
        if len(postData['last_name']) < 1:
            errors["last_name"] = "First name cannot be blank!"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name must contain at least two letters and contain only letters!"

        # ==================================

        # Email validations=================
        if len(postData['email']) < 1:
            errors['email'] = "Email cannot be blank!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email Address!"
        # elif check_duplicates(postData['email']):
        #     errors['email'] = "We encountered a problem."



class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


