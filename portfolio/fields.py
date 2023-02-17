from django import forms
from django.db import models
from django.core.validators import FileExtensionValidator

class SVGField(models.FileField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(FileExtensionValidator(['svg']))

    def formfield(self, **kwargs):
        defaults = {'widget': forms.ClearableFileInput}
        defaults.update(kwargs)
        return super().formfield(**defaults)
