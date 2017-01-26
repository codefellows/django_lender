from django import forms
from books.models import Book


class LoanForm(forms.ModelForm):
    """A form for loaning a book to a registered Patron."""

    class Meta:
        model = Book
        fields = ["borrower"]
