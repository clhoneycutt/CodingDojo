from django.db import models

class productManager(models.Manager):
    def validate(self, postData):
        errors = []
        if int(postData['numPurchase']) > int(postData['numAvail']):
            errors.append('Not enough in stock')
        return errors

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    numAvail = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = productManager()
