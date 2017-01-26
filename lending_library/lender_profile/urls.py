"""The URLs for the lender_profile app."""
from django.conf.urls import url
from lender_profile.views import (
    profile_view,
    ProfileView
)

urlpatterns = [
    url(r'$', profile_view, name="auth_profile"),
    url(r'(?P<username>\w+)/$', ProfileView.as_view(), name="user_profile")
]
