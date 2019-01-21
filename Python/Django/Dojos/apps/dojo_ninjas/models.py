from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    desc = models.TextField(default="")
class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)



# Create 3 dojos
# 1) Dojo.objects.create(name="CodingDojo Silicon Valley",city="Mountain View",state="CA")
# 2) Dojo.objects.create(name="CodingDojo Seattle",city="Seattle",state="WA")
# 3) Dojo.objects.create(name="CodingDojo New York",city="New York",state="NY")

# Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
# deleted_dojos = Dojo.objects.get(id=1)
# deleted_dojos = Dojo.objects.get(id=2)
# deleted_dojos = Dojo.objects.get(id=3)

# Create 3 additional dojos by using Dojo.objects.create
# 1) Dojo.objects.create(name="CodingDojo Austin",city="Austin",state="TX")
# 2) Dojo.objects.create(name="CodingDojo Chicago",city="Chicago",state="IL")
# 3) Dojo.objects.create(name="CodingDojo Online",city="Online",state="Internet")

# Create 3 ninjas that belong to the first dojo you created.
# 1) Ninja.objects.create(first_name="Chris",last_name="Hone",dojo=Dojo.objects.get(id=1))
# 2) Ninja.objects.create(first_name="Chris",last_name="Davila",dojo=Dojo.objects.get(id=1))
# 3) Ninja.objects.create(first_name="Ray",last_name="O",dojo=Dojo.objects.get(id=1))

# Create 3 more ninjas and have them belong to the second dojo you created.
# 1) Ninja.objects.create(first_name="Donald",last_name="Trump",dojo=Dojo.objects.get(id=2))
# 2) Ninja.objects.create(first_name="Barack",last_name="Obama",dojo=Dojo.objects.get(id=2))
# 3) Ninja.objects.create(first_name="Chuck",last_name="Norris",dojo=Dojo.objects.get(id=2))

# Create 3 more ninjas and have them belong to the third dojo you created.
# 1) Ninja.objects.create(first_name="Duane",last_name="Johnson",dojo=Dojo.objects.get(id=3))
# 2) Ninja.objects.create(first_name="Hulk",last_name="Hogan",dojo=Dojo.objects.get(id=3))
# 3) Ninja.objects.create(first_name="Formerly",last_name="Prince",dojo=Dojo.objects.get(id=3))

# Be able to retrieve all ninjas that belong to the first Dojo
# Ninja.objects.filter(dojo=Dojo.objects.first()

# Be able to retrieve all ninjas that belong to the last Dojo
# Ninja.objects.filter(dojo=Dojo.objects.last())