"""lending_library URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from lending_library.views import (
    home_view,
)

import books.urls as book_urls
from books.models import Book

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView, DetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name="home"),
    url(r'^profile/', include("lender_profile.urls")),
    url(r"^books/", include(book_urls)),

    url(r"^test/(?P<color>\w+)/(?P<number>\d+)$",
        TemplateView.as_view(template_name="potato/test.html"),
        name="test"),

    url(r"^this_book/(?P<pk>\d+)", DetailView.as_view(
        template_name="potato/test.html",
        model=Book
    ))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
