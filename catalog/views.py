from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Publisher, Review

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"

class PublisherListView(ListView):
    model = Publisher
    template_name = "publisher_list.html"
    context_object_name = "publishers"

class ReviewListView(ListView):
    model = Review
    template_name = "review_list.html"
    context_object_name = "reviews"