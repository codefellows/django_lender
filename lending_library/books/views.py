"""Views for the book app."""
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, CreateView
from django.urls import reverse_lazy

from books.forms import LoanForm
from books.models import Book

# Create your views here.


def book_list(request):
    """List books."""
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


class NewBook(CreateView):
    """Create a new book."""

    template_name = "books/add_book.html"
    model = Book
    fields = [
        "title", "author", "publisher", "isbn",
        "year", "cover_image", "status"
    ]
    success_url = reverse_lazy("book_list")


class RemoveBook(DeleteView):
    """Remove a book."""

    template_name = "books/remove_book.html"
    model = Book
    success_url = reverse_lazy("book_list")


def loan_book(request, pk):
    """Lend a book out to a user."""
    book = Book.objects.get(pk=pk)

    if request.POST and request.method == "POST":
        form = LoanForm({"borrower": request.POST["borrower"]}, instance=book)
        form.save()
        book.status = "checked out"
        book.save()
        return redirect(reverse_lazy("book_list"))

    form = LoanForm(instance=book)
    return render(
        request,
        "books/lend_book.html",
        {"form": form, "book": book}
    )
