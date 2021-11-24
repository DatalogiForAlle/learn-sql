from django.shortcuts import render
from .forms import SqlForm
from .models import City, Customer

def home(request):
    context = {}

    if request.method == "POST":
        form = SqlForm(request.POST)
        if form.is_valid():
            sql = form.cleaned_data['sql']
            context['sql_success'] = True
            results = ""

            if sql.lower() == 'select * from customer':
                results = Customer.objects.all().values()

            elif sql.lower() == 'select * from city':
                results = City.objects.all().values()

            else:
                context['sql_error'] = True

            context["results"] = results


    elif request.method == "GET":
        form = SqlForm(initial={'sql': 'SELECT * FROM customer'})

    context['form'] = form

    return render(request, "learnsql/home.html", context)
