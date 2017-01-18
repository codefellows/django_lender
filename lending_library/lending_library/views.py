from django.shortcuts import render


def home_view(request):
    """The home view."""
    return render(request,
                  "potato/home.html",
                  {"beg_for_it": "PLEASE"}
                  )


def test_view(request, num=None, word=None):
    return render(request,
                  "potato/home.html",
                  {"beg_for_it": "PLEASE",
                   "num": num,
                   "word": word}
                  )
