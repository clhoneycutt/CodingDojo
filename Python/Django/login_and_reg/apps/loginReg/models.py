from django.db import models
import bcrypt
import re

class UserManager(models.Manager):



    def regValidate(self, postData):

        def checkDuplicates(email):
            users = User.objects.all()
            for user in users:
                if user.email == email:
                    return True
            return False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        PW_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')

        print(postData)

        errors = {
            'first_name': [],
            'last_name': [],
            'emailReg': [],
            'passwordReg': [],
            'confPassword': [],
        }

        if len(postData['first_name']) < 1:
            errors['first_name'].append("First name field cannot be empty.")
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'].append("First name must contain at least two letters and contain only letters.")

        if len(postData['last_name']) < 1:
            errors['last_name'].append("Last name field cannot be empty.")
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'].append("Last name must contain at least two letters and contain only letters.")

        emailReg = postData['emailReg']
        if len(postData['emailReg']) < 1:
            errors['emailReg'].append("Email cannot be empty.")
        elif not EMAIL_REGEX.match(postData['emailReg']):
            errors['emailReg'].append("We have encountered a problem.")        
        elif checkDuplicates(emailReg):
            errors['emailReg'].append("We have encountered a problem.")

        if len(postData['passwordReg']) < 1:
            errors['passwordReg'].append("Password cannot be empty.")
        elif not PW_REGEX.match(postData['passwordReg']):
            errors['passswordReg'].append("Password must be 8 characters minimum and container only upper case and lower case letters, numbers and these special characters: @#$%^&+=")

        if len(postData['confPassword']) < 1:
            errors['confPassword'].append("Please confirm your password.")
        elif postData['confPassword'] != postData['passwordReg']:
            errors['confPassword'].append("Your passwords must match.")
    
        return errors

    def loginValidate(self, postData):
        email = postData['emailLogin']
        user = User.objects.filter(email=email)
        
        errors = {
            'emailLogin': [],
            'pwLogin': [],
        }

        if len(user) < 1:
            errors['emailLogin'].append("Email not found, please register!")



class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    pwhash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
