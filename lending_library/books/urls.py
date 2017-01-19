from django.conf.urls import url, include
from books.views import book_list

urlpatterns = [
    url(r"^$", book_list, name="book_list")
]