from django.shortcuts import render
from django.forms import modelformset_factory
from alerts.models import Trip

# Create your views here.

def index(request):
    TripsFormSet = modelformset_factory(Trip, fields = ('toAddress', 'fromAddress', 'arrivalTime', 'bufferMinutes', 'nextTrip', 'repeatsMonday', 'repeatsTuesday', 'repeatsWednesday', 'repeatsThursday', 'repeatsFriday', 'repeatsSaturday', 'repeatsSunday', 'notificationEmail'))
    if request.method == 'POST':
        formset = TripsFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            #what
    else:
        formset = TripsFormSet()
    return render(request, 'index.html', {'formset': formset})