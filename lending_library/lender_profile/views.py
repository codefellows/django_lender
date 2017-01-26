from django.shortcuts import render
from django.views.generic import DetailView
from lender_profile.models import PatronProfile

# Create your views here.

def profile_view(request):

    return render(request, "lender_profile/detail.html", {})


# class ProfileView(DetailView):

#     template_name = "lender_profile/detail.html"
#     model = PatronProfile
#     slug_field = "user__username"
