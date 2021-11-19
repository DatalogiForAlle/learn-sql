from django.shortcuts import render
from .forms import SqlForm
from django.db import connection


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

            try:
                cursor.execute(form.cleaned_data['sql'])
                results = dictfetchall(cursor)
                context["results"] = results
                context['sql_succes'] = True

            except:
                context['sql_error'] = True

    elif request.method == "GET":
        form = SqlForm(initial={'sql': 'SELECT * FROM customer'})

    context['form'] = form

    return render(request, "learnsql/home.html", context)
