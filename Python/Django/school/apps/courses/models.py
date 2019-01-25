from django.db import models

class courseManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['name']) < 5:
            errors.append("Course name must be at least 5 characters")
        if len(postData['desc']) < 15:
            errors.append("Course description must be at least 15 characters")
        return errors


class Description(models.Model):
    content = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = courseManager()

class Course(models.Model):
    description = models.OneToOneField(Description, related_name='course')
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = courseManager()