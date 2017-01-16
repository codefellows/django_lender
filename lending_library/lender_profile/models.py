from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save # <-- after saving a thing, do a thing
from django.dispatch import receiver # <-- listen for a thing to be done

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


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    new_profile = PatronProfile(user=instance)
    new_profile.money_owed = 0.0
    new_profile.save()
