from os import terminal_size
from django.db import models

class Tweet(models.Model):
    #id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)
