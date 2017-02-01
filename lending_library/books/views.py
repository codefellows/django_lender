"""Views for the book app."""
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from books.forms import LoanForm
from books.models import Book

# Create your views here.


def book_list(request):
    """List books."""
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


class NewBook(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create a new book."""

    template_name = "books/add_book.html"
    model = Book
    fields = [
        "title", "author", "publisher", "isbn",
        "year", "cover_image", "status"
    ]
    success_url = reverse_lazy("book_list")
    login_url = reverse_lazy("login")
    permission_required = "lender_books.add_book"


class RemoveBook(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Remove a book."""

    template_name = "books/remove_book.html"
    model = Book
    success_url = reverse_lazy("book_list")
    login_url = reverse_lazy("login")
    permission_required = ["lender_books.potato"]


@login_required(login_url=reverse_lazy("login"))
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


@login_required(login_url=reverse_lazy("/login"))
@csrf_exempt
def return_book(request, pk):
    """Lend a book out to a user."""
    book = Book.objects.get(pk=pk)

    if request.method == "POST" and request.POST["return_me"] == "true":
        profile = book.borrower
        profile.borrowed.remove(book)
        profile.save()
        book.status = "available"
        book.save()
        return redirect(reverse_lazy("book_list"))

    return render(
        request,
        "books/return_book.html",
        {"book": book}
    )


class TagListView(ListView):
    template_name = "books/tag_list.html"
    slug_field_name = "tag"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(tags__slug=self.kwargs.get("tag")).all()

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("tag")
        return context
