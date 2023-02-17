from django.db import models
from django.db.models.fields import CharField, URLField, IntegerField
from django.db.models.fields.files import ImageField
from .fields import SVGField

class Project(models.Model):
    title = CharField(max_length = 100)
    description = CharField(max_length = 400)
    image = ImageField(upload_to="portfolio/images/projects")
    url_git = URLField(blank=True)
    url_deploy = models.URLField(blank=True, null=True, help_text="Link opcional al despliegue del proyecto")

    
class Technologie(models.Model):
    title = CharField(max_length = 100)
    description = IntegerField(default=0)
    image = SVGField(upload_to="portfolio/images/tecnhnologies")
