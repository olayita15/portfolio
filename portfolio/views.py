from django.shortcuts import render
from .models import Project, Technologie
from django.urls import reverse
from django.utils.translation import activate, gettext
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.conf import settings



def Home(request):
    projects = Project.objects.all()
    technologies = Technologie.objects.all()
    return render(request,'home.html', {'projects':projects, 'technologies':technologies})


def set_language(request):
    language = request.GET.get('language')
    if language:
        activate(language)
        response = redirect(request.META.get('HTTP_REFERER'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response
    else:
        return HttpResponseBadRequest(gettext('Language code not found.'))
