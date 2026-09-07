from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("publishers/", views.PublisherListView.as_view(), name="publisher_list"),
    path("reviews/", views.ReviewListView.as_view(), name="review_list"),
]