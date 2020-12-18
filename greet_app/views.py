from django.shortcuts import render, redirect
# Create your views here.
from greet_app.forms import GreetingForm
from greet_app.models import Person


def insert(request):
    form = GreetingForm()
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    return render(request, 'insert.html')


def show(request):
    greet = Person.objects.all()
    return render(request, 'show.html', {'greet': greet})


def delete(request, id):
    greet = Person.objects.get(id=id)
    greet.delete()
    return redirect('/show')


def update(request, id):
    greet = Person.objects.get(id=id)
    form = GreetingForm(request.POST, instance=greet)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'update.html', {'greet': greet})
