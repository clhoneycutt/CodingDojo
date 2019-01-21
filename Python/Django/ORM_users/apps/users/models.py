from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Know how to retrieve all users.
# 1) User.objects.all()

# Know how to get the last user.
# 2) User.objects.last()

# Create a few records in the users
# 3) User.objects.create(first_name="Chris", last_name="Hone", age="35", email="test@test.com", password="password")

# Know how to get the first user.
# 4) User.objects.first()

# Know how to get the users sorted by their first name (order by first_name DESC)
# 5) User.objects.order_by("-first_name")

# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
# 6) currentUser = User.objects.get/(id=3)
#    currentUser.last_name = "Something_else"
#    currentUser.save()

# Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
# 7) currentUser = User.objects.get/(id=4)
#    currentUser.delete()