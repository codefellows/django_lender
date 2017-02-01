"""The URLs for the Book app."""
from django.conf.urls import url
from django.views.generic import DetailView

from books.models import Book
from books.views import (
    book_list,
    NewBook,
    RemoveBook,
    loan_book,
    return_book,
    TagListView
)


urlpatterns = [
    url(r"^$", book_list, name="book_list"),
    url(r"^(?P<pk>\d+)$", DetailView.as_view(
        template_name="books/book_detail.html",
        model=Book,
        context_object_name="book"
    ), name="book_detail"),
    url(r"^new$", NewBook.as_view(), name="add_book"),
    url(r"^remove/(?P<pk>\d+)$", RemoveBook.as_view(), name="remove_book"),
    url(r"^loan/(?P<pk>\d+)$", loan_book, name="loan_book"),
    url(r"^return/(?P<pk>\d+)$", return_book, name="return_book"),
    url(r"^tagged/(?P<tag>[-\w]+)/$", TagListView.as_view(), name="tag_list") 
]
