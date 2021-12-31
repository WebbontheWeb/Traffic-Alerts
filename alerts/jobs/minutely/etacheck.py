#go away please
import datetime
import os
import googlemaps
from django_extensions.management.jobs import MinutelyJob
from django.core.mail import send_mail
from alerts.models import *

gmaps = googlemaps.Client(key=os.environ['APIKEY'])

class Job(MinutelyJob):
    help = "Checks to see if the ETA is the time of arrival"

    def execute(self):
        print('Running...')
        trips = Trip.objects.filter(nextTrip=datetime.date.today()) #Imports model and brings in only ones needed to do today
        print(trips)
        for trip in trips:
            data = gmaps.distance_matrix(trip.fromAddress,trip.toAddress, departure_time = 'now')
            transitTime = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
            ETA = datetime.timedelta(0, (trip.bufferMinutes*60) + transitTime) + datetime.datetime.now()
            ToA = datetime.datetime.combine(datetime.datetime.now(),trip.arrivalTime)
            print(ToA)

            repeatsDays = [trip.repeatsMonday, trip.repeatsTuesday, trip.repeatsWednesday, trip.repeatsThursday, trip.repeatsFriday, trip.repeatsSaturday, trip.repeatsSunday]
            #easier to move through array

            if ToA <= ETA:
                send_mail(
                    'LEAVE NOW', #subject
                    'RUN-- THIS IS YOUR FINAL WARNING',
                    os.environ['FROMEMAIL'], #from
                    [trip.notificationEmail], #to
                    fail_silently=False,
                )

                #setting the next trip
                tomorrow = datetime.date.today()
                while trip.nextTrip == datetime.date.today():
                    tomorrow = tomorrow + datetime.timedelta(days=1)
                    if repeatsDays[tomorrow.weekday()] == True:
                        trip.nextTrip = tomorrow #Queues the next trip
                        trip.save()
                        print(tomorrow)

        pass
