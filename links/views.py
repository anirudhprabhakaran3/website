from django.shortcuts import redirect, get_object_or_404
from links.models import ShortLink


def unshorten(request, slug):
    short = get_object_or_404(ShortLink, slug=slug)
    return redirect(short.target)
