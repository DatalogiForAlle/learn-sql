from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from .models import Customer
from django.contrib.auth.decorators import login_required
#from django.contrib import messages
from .forms import SqlForm
from django.db import connection

# https: // www.youtube.com/watch?v = _TtBxvYwoHY & t = 472s


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def home(request):
    context = {}

    if request.method == "POST":
        form = SqlForm(request.POST)
        if form.is_valid():

            cursor = connection.cursor()
            cursor.execute(form.cleaned_data['sql'])
            results = dictfetchall(cursor)

            context["results"] = results

    elif request.method == "GET":
        form = SqlForm(initial={'sql': 'SELECT * FROM customer'})

    context['form'] = form

    return render(request, "learnsql/home.html", context)
