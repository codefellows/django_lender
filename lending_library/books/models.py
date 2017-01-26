"""The book model."""
from django.db import models
from lender_profile.models import PatronProfile

# Create your models here.


class Book(models.Model):
    """The book model."""

    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.IntegerField(blank=True, null=True)

    YEARS = [(str(num), str(num)) for num in range(2018, 1000, -1)]
    year = models.CharField(max_length=4, choices=YEARS)
    cover_image = models.ImageField(upload_to="book_covers")

    borrower = models.ForeignKey(
        PatronProfile,
        related_name="borrowed",
        blank=True,
        null=True
    )

    BOOK_STATUS = [
        ("available", "Available"),
        ("checked out", "Checked Out")
    ]
    status = models.CharField(
        max_length=20,
        choices=BOOK_STATUS,
        default="available"
    )

    def __str__(self):
        """String representation of the book."""
        return self.title
