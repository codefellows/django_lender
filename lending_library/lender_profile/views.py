from django.shortcuts import render
from django.views.generic import DetailView
from lender_profile.models import PatronProfile

# Create your views here.


def profile_view(request):
    """Get this user's profile."""
    profile = PatronProfile.objects.get(user=request.user)
    return render(request, "lender_profile/detail.html", {"profile": profile})


class ProfileView(DetailView):
    """For viewing an individual profile."""

    template_name = "lender_profile/detail.html"
    model = PatronProfile
    slug_field = "user__username"
    slug_url_kwarg = "username"
