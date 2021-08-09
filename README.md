# geoDjango

## Summary
Django web application with the geodjango extention and postgreSQL database with postGIS extention. Created as a proof of concept for a Citizen Science app during a summerproject at C4iR Ocean.

The app has two different types of users: Citizen Scientists and Researchers

Citizen scientist can upload observations documented by images of marine species related to projects created by researchers. 
Timestamp and location of an observation is extracted from the image by use of python libraries Pillow and GPSPhoto. 

Observations and areas of interest are rendered on a map using Mapbox GL JS.

In addition, a machine learning model for image classification was created using Tensorflow to differentiate between blue mussels and pacific oysters.

## Run the Application
To run the application you need a postGIS database installed locally. Clone the project and change the database settings in iMap/settings.py
