from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from users.models import CitizenScientist, Scientist
from GPSPhoto import gpsphoto
from PIL import Image
from PIL.ExifTags import TAGS
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.


class NatureReserve(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    location = models.PointField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=100)


class ObservationTest(models.Model):
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="observations/")
    obs_date = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    coordinate = models.PointField(blank=True, null=True)

    user = models.ForeignKey(
        CitizenScientist, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        super(ObservationTest, self).save(*args, **kwargs)
        img_data = gpsphoto.getGPSData(self.image.path)

        if img_data is None:
            raise ValidationError(
                {'image': _('The image does not contain any GPS info')})
        try:
            self.lat = img_data['Latitude']
            self.lon = img_data['Longitude']
        except KeyError as e:
            raise ValidationError(
                {'image': _("Can't find coordinates of image")})

        if "Altitude" in img_data.keys():
            self.altitude = img_data['Altitude']
        else:
            self.altitude = 0.0

        img_exif_data = Image.open(self.image).getexif()
        for key, val in img_exif_data.items():
            img_exif_data[TAGS.get(key)] = val

        try:
            self.obs_date = datetime.datetime.fromisoformat(
                img_exif_data['DateTime'].replace(':', '-', 2))
        except KeyError as e:
            return

        self.coordinate = Point([self.lon, self.lat])

        if self.inAreaOfInterest():
            print(f"User points = {self.user.points}")
            self.user.points += 1
            self.user.save()
            print(f"User points updated?: {self.user.points}")

        return super(ObservationTest, self).save(*args, **kwargs)

    def clean(self) -> None:
        super().clean()

        try:
            exif_dir = Image.open(self.image).getexif()
        except FileNotFoundError as e:
            print("Could not find the file.")
            raise ValidationError({'image': _('Could not find the image')})

        for key, val in exif_dir.items():
            exif_dir[TAGS.get(key)] = val

        try:
            timestamp = datetime.datetime.fromisoformat(
                exif_dir['DateTime'].replace(':', '-', 2))
        except KeyError as e:
            print("{}".format(e))
            raise ValidationError(
                {'image': _("The image doesn't contain any timestamp")})

    def inAreaOfInterest(self, *args, **kwargs):
        areas_lst = AreaOfInterest.objects.all()
        for obj in areas_lst:
            print(obj.name)
            # Check if this object is already linked to the area
            if obj.area.contains(self.coordinate) and self not in obj.observations.all():
                obj.observations.add(self)
                print(f"Point in area: {obj.name}")
                return True
        return False


class AreaOfInterest(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)
    area = models.PolygonField()
    scientist = models.ForeignKey(
        Scientist, on_delete=models.CASCADE, null=True)
    observations = models.ManyToManyField(ObservationTest)


"""
USERS AND OBSERVATIONS

Each observation should be related to a specific user. In addition, the observation must contain
some sort of information about what has been observed, i.e what species. 

Further, there should be scientist users who could create areas on the map which they are interested
in collecting data. If the user collects data whithin these areas, they should be rewarded with some
amount of points depending on the "importance or the observation. 
    - This indicates that AreaOfInterest is related to a researcher / scientist. 

HOW TO RELATED AND CREATE THIS KIND OF DATABASE

    - Observation containing a user field
    - User should have list of observations. 

"""
