from django.db import models

class Chant(models.Model):
    title = models.CharField(max_length=200)
    volpiano = models.CharField(max_length=1000)
    full_text = models.CharField(max_length=1000)
