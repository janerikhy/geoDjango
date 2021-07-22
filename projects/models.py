from users.models import CitizenScientist, Scientist
from django.db import models
from observations.models import AreaOfInterest
from challenges.models import Challange

from django.core.validators import FileExtensionValidator
# Create your models here.


class Species(models.Model):
    latin_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250, blank=True, null=True)
    common_name = models.CharField(max_length=250)
    taxon_id = models.IntegerField(blank=False, null=True)

    def __str__(self) -> str:
        return f"Species: {self.common_name} [Taxon id: {self.taxon_id}]"


class Project(models.Model):
    """
    Project model for researchers. The model will store the location and other relevant features of a project.
    """
    name = models.CharField(blank=False, max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/imgs")
    challenges = models.ManyToManyField(
        Challange, default=Challange._default_value())
    participants = models.ManyToManyField(CitizenScientist, blank=True)
    creators = models.ManyToManyField(Scientist)
    video = models.FileField(upload_to="projects/videos",
                             validators=[FileExtensionValidator(['MOV', 'mp4', 'avi', 'mov', 'MP4'], 'The file format is not accepted')])
    species = models.ManyToManyField(Species)
    areas = models.ManyToManyField(
        AreaOfInterest)
    start_time = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True)
    end_time = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True)

    is_public = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Project[id={self.pk}]: {self.name}"

    def get_leaderboard(self, **kwargs):
        pass
