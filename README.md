# Traffic Alerts
### Calls the Google Maps API to email you when you need to leave

I wanted something that would tell me when I need to start my commute to
school each day, so I thought this might be handy

### Description
A user inputs their trips- including the to and from addresses, preferred time of arrival, how much of a buffer of extra time you want,  whether this trip repeats on certain weekdays, etc.- and Django adds them to a database of all the trips.  Every minute a job is run that pulls in the trips from the database that are happening on the current day and checks whether it's time to leave or not.  Once it is it emails a notification and queues the next instance of that trip if it's reoccuring.

## Setting Up
The dockerfile is included so if you launch Traffic Alerts in Visual Studio Code with the Remote-Containers extension downloaded
it should automatically install what's needed

### Adding to Database
The easiest way to just to launch the django webserver and log into the admin portal, which will require making a
superuser

### .env File
A .env file with 
APIKEY="your google api key"
FROMEMAIL="your email to send emails from"
EMAILPASSWORD="your email's app passwork"
EMAILPORT="email port"
EMAILHOST="email host"

### Running
Once the database and .env file are up and running, you should just be able to
`honcho start` and it should start fine


## Future Work
Traffic Alerts is completely functional in it's current state, but I'd certainly like to clean it up a little

-Currently it will only call the Maps API on the day of the trip, but if it's calling it every minute that can still 
add up pretty quickly: adding an algorithim that limits the calls to only what's actually nessesary would make this much more practical to deploy 

-Find a better way to have it consistantly running: currently I'm just using Honcho to run it continuously and having it sleep for 60 seconds
between runs which works but it's the most elegant solution

-Create a better way of inputting into the database: using the django's webserver or inputting them manually isn't ideal
