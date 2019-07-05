from django.db import models
import re


# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!! 
# (just parts, like request.POST)
class UserManager(models.Manager):
    def check_duplicates(self, email):
        alreadyExists = User.objects.filter(email=email)
        if alreadyExists:
            return True
        else:
            return False

    def validate(self, postData):
        # This should be broken up into separate validation requests, but isn't for the sake of time.

        errors = []
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        # First name validations============
        if len(postData['first_name']) < 0:
            errors.append("First name cannot be blank") 
        elif len(postData["first_name"]) > 60:
            errors.append("First name cannot be longer than 60 characters")
        elif not NAME_REGEX.match(postData['first_name']):
            errors.append("First name must contain at least two letters and only contain letters.")

        # ==================================

        # Last name validations=============
        if len(postData['last_name']) < 1:
            errors.append("First name cannot be blank!")
        elif not NAME_REGEX.match(postData['last_name']):
            errors.append("Last name must contain at least two letters and contain only letters!")

        # ==================================

        # Email validations=================
        if len(postData['email']) < 1:
            errors.append("Email cannot be blank!")
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid Email Address!")
        elif self.check_duplicates(postData['email']):
            errors.append("We encountered a problem.")
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


