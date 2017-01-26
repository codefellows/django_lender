"""."""
from django.shortcuts import render
from lender_profile.models import PatronProfile


def home_view(request):
    """The home view."""
    profiles = PatronProfile.objects.all()
    return render(request,
                  "potato/home.html",
                  {"patrons": profiles}
                  )
