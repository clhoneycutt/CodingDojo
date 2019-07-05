from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    name = models.CharField(max_length=60)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name='uploaded_books')
    liked_users = models.ManyToManyField(User, related_name='liked_books')







# For your assignment:
# Create the appropriate models and the appropriate relationship.  Design your models so that the following command would be supported

# Book.objects.first().uploader - this should return the user who uploaded the book
# User.objects.first().uploaded_books - this should return all the books that are uploaded by the first user
# Book.objects.first().liked_users - this should return all the users who liked the first book
# User.objects.first().liked_books - this should return all the books that were liked by the first user

# Create 3 different user accounts
# User.objects.create(first_name="Chris",last_name="Hone",email="test@test.com")
# User.objects.create(first_name="Spider",last_name="man",email="spiderman@test.com")
# User.objects.create(first_name="Bat",last_name="man",email="batman@test.com")

# Have the first user create/upload 2 books.
# Book.objects.create(name="C sharp", desc="A book about C sharp", uploader=User.objects.get(id=1))
# Book.objects.create(name="Python", desc="A book about Python", uploader=User.objects.get(id=1))

# Have the second user create/upload 2 other books.
# Book.objects.create(name="The art of webslinging", desc="spideysense!", uploader=User.objects.get(id=2))
# Book.objects.create(name="How to get a dozen remakes of your movie", desc="With great power...", uploader=User.objects.get(id=2))

# Have the third user create/upload 2 other books.
# Book.objects.create(name="MY PARENTS ARE DEAD", desc="ahhhhhhhh", uploader=User.objects.get(id=3))
# Book.objects.create(name="Guide to a modern batcave", desc="hint: live bats!", uploader=User.objects.get(id=3))

# Have the first user like the last book and the first book
# user_liking = User.objects.get(id=1)
# book_liked1 = Book.objects.get(id=1)
# book_liked2 = Book.objects.last()
# user_liking.liked_books.add(book_liked1, book_liked2) 

# Have the second user like the first book and the third book
# user_liking = User.objects.get(id=2)
# book_liked1 = Book.objects.first()
# book_liked2 = Book.objects.get(id=3)
# user_liking.liked_books.add(book_liked1, book_liked2)

# Have the third user like all books
# user_liking = User.objects.get(id=3)
# books_liked = Book.objects.all()
# for book in books_liked:
#   user_liking.liked_books.add(book)

# Display all users who like the first book
# book = Book.objects.get(id=1)
# book.liked_users.all()


# Display the user who uploaded the first book
# book.uploader

# Display all users who like the second book
# book = Book.objects.get(id=2)
# book.liked_users.all()

# Display the user who uploaded the second book
# book.uploader