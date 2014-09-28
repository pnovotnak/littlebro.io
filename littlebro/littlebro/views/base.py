from django.http import HttpResponseNotFound
from django.template.loader import render_to_string
from django.template import RequestContext


def client_error(request):
    return HttpResponseNotFound(
        render_to_string(
            "400.html",
            context_instance=RequestContext(request)
        )
    )


def page_not_found(request):
    return HttpResponseNotFound(
        render_to_string(
            "404.html",
            context_instance=RequestContext(request)
        )
    )


def server_error(request):
    return HttpResponseNotFound(
        render_to_string(
            "500.html",
            context_instance=RequestContext(request)
        )
    )
