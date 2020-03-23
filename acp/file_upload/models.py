from django.db import models
from django.db.models.signals import post_save, pre_save
import os
from .validators import validate_file_extension


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(
        upload_to="documents/", validators=[validate_file_extension]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    def filename(self):
        return os.path.basename(self.document.name)


class Emotion(models.Model):
    happy = models.IntegerField()
    panic = models.IntegerField()
    bored = models.IntegerField()
    frustrated = models.IntegerField()

    def __str__(self):
        return self.happy
