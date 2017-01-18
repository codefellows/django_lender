from django.conf.urls import url
from lender_profile.views import (
    profile_view
)

urlpatterns = [
    url(r'^$', profile_view, name="profile")
]
