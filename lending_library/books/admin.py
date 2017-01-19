from django.contrib import admin
from books.models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    """Tell the Django admin how to display books."""

    list_display = ("title", "year")


admin.site.register(Book, BookAdmin)
