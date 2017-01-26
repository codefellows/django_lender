"""The URLs for the Book app."""
from django.conf.urls import url
from books.models import Book
from books.views import book_list
from django.views.generic import DetailView

urlpatterns = [
    url(r"^$", book_list, name="book_list"),
    url(r"^(?P<pk>\d+)$", DetailView.as_view(
        template_name="potato/test.html",
        model=Book
    ))
]
