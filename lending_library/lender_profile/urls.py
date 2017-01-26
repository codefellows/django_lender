"""The URLs for the lender_profile app."""
from django.conf.urls import url
from lender_profile.views import (
    profile_view,
    # ProfileView
)

urlpatterns = [
    url(r'^$', profile_view, name="profile")
    # url(r'^(?P<slug>\w+)$', ProfileView.as_view(), name="profile")
]
