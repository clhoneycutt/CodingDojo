from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Author, Book, Review
from ..users.models import User

def index(request):

    context = {
        'reviews': Review.objects.recentReviews(),
        'books': Book.objects.all()
    }

    return render(request, 'books/index.html', context)

def new(request):

    context = {
        'authors': Author.objects.all()
    }

    return render(request, 'books/new.html', context)

def show(request, bookid):

    try:
        context = {
            'bookid': bookid,
            'reviews': Review.objects.filter(book_id=bookid),
            'book': Book.objects.get(id=bookid)
        }

        return render(request, 'books/show.html', context)
    except:
        error = "We have encountered a problem showing the book. Please contact an administrator"
        messages.error(request, error)
        return redirect('books:index')


def createBook(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
        return redirect('main:index')


    if request.method == 'POST':
        newBook = request.POST


        authorInfo = {
            'existingauthors': newBook['existingauthors'],
            'newauthor': newBook['newauthor']
        }
        errors = Author.objects.authorValidate(authorInfo)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('books:new')
        if newBook['existingauthors'] == "addauthor":
            authorInfo['name'] = newBook['newauthor']
        else:
            authorInfo['name'] = newBook['existingauthors']
        authorInfo.pop('existingauthors', None)
        authorInfo.pop('newauthor', None)



        bookInfo = {
            'title': newBook['title'],
            'author': authorInfo['name']
        }
        errors = Book.objects.bookValidate(bookInfo)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('books:new')


        reviewInfo = {

            'review': newBook['review'],
            'rating': int(newBook['rating'])
        }
        errors = Review.objects.reviewValidate(reviewInfo)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('books:new')



        Author.objects.addAuthor(authorInfo)
        Book.objects.addBook(bookInfo)
        reviewInfo['book'] = Book.objects.last()
        reviewInfo['reviewer'] = request.session['userid']
        Review.objects.addReview(reviewInfo)

    addedBook = Book.objects.last()
    bookid = addedBook.id
    return redirect('books:show', bookid)


def addReview(request, bookid):
    review = request.POST
    reviewInfo = {
        'reviewer': request.session['userid'],
        'book': Book.objects.get(id=bookid),
        'rating': review['rating'],
        'review': review['review']
    }

    errors = Review.objects.reviewValidate(reviewInfo)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('books:show', bookid)


    Review.objects.addReview(reviewInfo)
    return redirect('books:show', bookid)   

def deleteReview(request, bookid, reviewid):
    Review.objects.deleteReview(reviewid)
    
    return redirect('books:show', bookid)


