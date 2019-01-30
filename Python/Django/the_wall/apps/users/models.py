from django.db import models

from django.db import models
import bcrypt
import re

class UserManager(models.Manager):

    def regValidate(self, postData):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        PW_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')

        errors = []

        if len(postData['first_name']) < 1:
            errors.append("First name field cannot be empty.")
        if not NAME_REGEX.match(postData['first_name']):
            errors.append("First name must contain at least two letters and contain only letters.")

        if len(postData['last_name']) < 1:
            errors.append("Last name field cannot be empty.")
        if not NAME_REGEX.match(postData['last_name']):
            errors.append("Last name must contain at least two letters and contain only letters.")

        emailReg = postData['emailReg']
        if len(postData['emailReg']) < 1:
            errors.append("Email cannot be empty.")
        if not EMAIL_REGEX.match(postData['emailReg']):
            print('failed email regex')
            errors.append("We have encountered a problem.")
        existing_users = self.filter(email=emailReg)
        if existing_users:
            print('failed duplicate check')
            errors.append("We have encountered a problem.")

        if len(postData['passwordReg']) < 1:
            errors.append("Password cannot be empty.")
        if not PW_REGEX.match(postData['passwordReg']):
            errors.append("Password must be 8 characters minimum and container only upper case and lower case letters, numbers and these special characters: @#$%^&+=")

        if len(postData['confPassword']) < 1:
            errors.append("Please confirm your password.")
        if postData['confPassword'] != postData['passwordReg']:
            errors.append("Your passwords must match.")
        print(errors)
        return errors

    def loginValidate(self, postData):
        
        email = postData['emailLogin']
        password = postData['pwLogin']
        
        errors = []

        if len(email) < 1:
            errors.append("Email cannot be blank")
            return errors
        if len(password) < 1:
            errors.append("Password cannot be blank")
            return errors            

        user = User.objects.filter(email=email)
        if len(user) < 1:
            errors.append("We have encountered a problem")
        
        return errors

    def attemptLogin(self, postData):
        email = postData['emailLogin']
        user = User.objects.get(email=email)
        password = postData['pwLogin']

        pwCheck = bcrypt.checkpw(password.encode(), user.pwhash.encode())
        print(pwCheck)
        if pwCheck:
            return True
        else:
            return False
        


    
    def createUser(self, postData):
        pwhash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(
            first_name=registeringUser['first_name'],
            last_name=registeringUser['last_name'],
            email=registeringUser['emailReg'],
            pwhash=pwhash
        )
        
    def pwCheck(self, user, password):
        if bcrypt.checkpw(password.encode(), user.pwhash.encode()):
            return True
        else:
            return False
        




class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    pwhash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
