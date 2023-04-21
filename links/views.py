from django.shortcuts import render, redirect, get_object_or_404
from links.models import ShortLink


# Create your views here.
def index(request):
    args = {}
    return render(request, "links/index.html", args)


def pattern_matcher(request, slug):
    short_link = get_object_or_404(ShortLink, slug=slug)
    return redirect(short_link.target)
