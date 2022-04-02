from django.db import models

class InputModel(models.Model):
    data = models.JSONField()