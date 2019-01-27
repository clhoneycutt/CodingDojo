from django.db import models

class UserManager(models.Manager):
    def validate(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        PW_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
        errors = {
            'first_name': [],
            'last_name': [],
            'email': [],
            'password': [],
            'confPassword': [],
        }

        if len(postData['first_name']) < 1:
            errors['first_name'].append("First name field cannot be empty")
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'].append("First name must contain at least two letters and contain only letters.")

        if len(postData['last_name']) < 1:
            errors['last_name'].append("Last name field cannot be empty")
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'].append("Last name must contain at least two letters and contain only letters.")

        if len(postData['emailReg']) < 1:
            errors['email'].append("Email cannot be empty.")
        elif not EMAIL_REGEX.match(postData['emailReg']):
            errors['email'].append("We have encountered a problem")



class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    pwhash = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
