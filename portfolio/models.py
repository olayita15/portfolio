from django.db import models
from django.db.models.fields import CharField, URLField, DecimalField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length = 100)
    description = CharField(max_length = 400)
    image = ImageField(upload_to="portfolio/images/projects")
    url_git = URLField(blank=True)
    url_deploy = URLField(blank=True)
    
class Technologie(models.Model):
    title = CharField(max_length = 100)
    description = DecimalField(max_digits=5, decimal_places=2)
    image = ImageField(upload_to="portfolio/images/tecnhnologies")
