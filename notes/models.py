from django.db import models
from django.conf import settings


# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note_header = models.CharField(max_length=128, default='')
    note_content = models.TextField(default='')
