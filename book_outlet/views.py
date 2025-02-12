from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
  books = Book.objects.all().orderBy('title')
  count = books.count()
  avg = books.aggregate(Avg('rating'))
  # print(books)
  
  return render(request, 'book_outlet/index.html', {
    'books': books
  })
  
def book_detail(request, slug):
  book = get_object_or_404(Book, slug=slug)
  
  return render(request, 'book_outlet/book.html', {
    'book': book
  })
