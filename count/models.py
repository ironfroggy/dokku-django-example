from django.db import models

class Count(models.Model):
    # this simply maintains the last count
    last_number = models.PositiveIntegerField(default=0)
