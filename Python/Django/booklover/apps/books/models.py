from django.db import models
from ..users.models import User


class authorManager(models.Manager):

    def authorValidate(self, authorInfo):
        errors = []

        if authorInfo['existingauthors'] == "addauthor" and len(authorInfo['newauthor']) < 1:
            errors.append("The author's name cannot be empty.")

        if authorInfo['existingauthors'] != 'addauthor':
            if len(authorInfo['newauthor']) > 0:
                errors.append('Unable to add a new author. Please set author dropdown to --add a new author--.')
        
        if authorInfo['existingauthors'] == 'addauthor':
            if authorInfo['newauthor']:
                if self.filter(name=authorInfo['newauthor']):
                    errors.append("That author already exists")

        return errors


    def addAuthor(self, authorInfo):
        self.create(name=authorInfo['name'])

class bookManager(models.Manager):
    
    def bookValidate(self, bookInfo):
        errors = []

        if len(bookInfo['title']) < 1:
            errors.append("The book title cannot be empty.")
        if self.filter(title__contains=bookInfo['title']):
            errors.append("This book is already in the database")
        
        return errors

    def addBook(self, bookInfo):
        self.create(title=bookInfo['title'], author=Author.objects.get(name=bookInfo['author']))



class reviewManager(models.Manager):
    
    def reviewValidate(self, reviewInfo):
        errors = []

        if len(reviewInfo['review']) < 1:
            errors.append("You must enter a review to add a book.")


        return errors

    def addReview(self,reviewInfo):
        
        self.create(reviewer=User.objects.get(id=reviewInfo['reviewer']), book=reviewInfo['book'], rating=reviewInfo['rating'], review=reviewInfo['review']) 

    def recentReviews(self):
        recentReviews = self.all().order_by("-created_at")[:3]
        
        return recentReviews

    def deleteReview(self, reviewid):
        goodbyeReview = self.get(id=reviewid)
        goodbyeReview.delete()



class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = authorManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = bookManager()


class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = reviewManager()