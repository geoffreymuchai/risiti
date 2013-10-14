from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.utils import timezone

from polls.models import Question, Choice


def index(request):
	render(request, 'risiti/index.html')
