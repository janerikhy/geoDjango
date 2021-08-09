from django.db.models.fields.reverse_related import ManyToOneRel
from users.models import CitizenScientist, Scientist
from django.contrib.gis.db import models
from observations.models import AreaOfInterest
from challenges.models import Challange
import datetime
from django.contrib.gis.geos import Polygon
import pytz
from django.core.validators import FileExtensionValidator
# Create your models here.


class Species(models.Model):
    latin_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250, blank=True, null=True)
    common_name = models.CharField(max_length=250)
    taxon_id = models.IntegerField(blank=False, null=True)

    def __str__(self) -> str:
        return f"Species: {self.common_name} [Taxon id: {self.taxon_id}]"


class Environment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)      # Max length set to 250 as it should be a short description

    def __str__(self):
        return self.name


class Organization(models.Model):
    """
    Organizations which researchers are connected to.
    """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    """
    Sponsors can contribute with different rewards such as free kayaking in 30 minutes etc.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)       # If they want to, they can promote themselves
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Reward(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(help_text="Describe the reward")
    distributor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Project model for researchers. The model will store the location and other relevant features of a project.
    """
    owner = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to=f"projects/images")
    challenges = models.ManyToManyField(
        Challange, default=Challange._default_value())
    participants = models.ManyToManyField(CitizenScientist, blank=True)
    video = models.FileField(upload_to="projects/videos",
                             validators=[FileExtensionValidator(['MOV', 'mp4', 'avi', 'mov', 'MP4'], 'The file format is not accepted')])
    species = models.ManyToManyField(Species)
    areas = models.ManyToManyField(
        AreaOfInterest)
    location = models.PolygonField(blank=True, null=True)    # Had to add this field if we want to create from scratch
    start_time = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True)
    end_time = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True) # Should be able to set ungoing as time

    organizers = models.ManyToManyField(Organization)
    rewards = models.ManyToManyField(Reward)

    environments = models.ManyToManyField(Environment)

    is_public = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Project[id={self.pk}]: {self.name}"


    def get_leaderboard(self, **kwargs):
        """
        Get leaderboard for the current project.

        - Check for users in the project.
        - Check if the observations from the user is in the correct
        - Check if the observation was done whitin the scope of this project.
        """
        pass

    def in_timerange(self, date: datetime.datetime, **kwargs) -> bool:
        return self.start_time <= date <= self.end_time

    def observation_is_valid(self, date, location) -> bool:
        return any([area.inArea(location) for area in self.areas.all()]) and self.in_timerange(date)

    def observation_data(self):
        print("Running observation_data()")
        data = {}
        min_date = self.start_time
        max_date = pytz.UTC.localize(datetime.datetime.today())
        date_iter = min_date
        while date_iter < max_date:
            date_str = date_iter.strftime("%m/%d/%y")
            data.setdefault(date_str, 0)
            date_iter += datetime.timedelta(days=1)
        print(f"Initialized data as: {data}")
        for area in self.areas.all():
            for obs in area.observations.all().order_by('-obs_date'):
                if self.in_timerange(obs.obs_date):
                    date_str = obs.obs_date.strftime("%m/%d/%y")
                    data.setdefault(date_str, 0)
                    data[date_str] += 1
        print(f"Final data dict: {data}")
        return data


    def find_challenges(self, **kwargs):
        """
        Find relevant challenges for this project.
        """
        pass