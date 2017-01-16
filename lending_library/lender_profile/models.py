from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class PatronProfile(models.Model):
    """The Library Patron and All Of Its Attributes."""

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    money_owed = models.DecimalField(
        max_digits=8, decimal_places=2
    )
    employed = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    library_id = models.UUIDField(default=uuid.uuid4, editable=False)
