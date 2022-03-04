from django.db import models
from datetime import datetime
class Post(models.Model):
    task = models.CharField(max_length =100000)
    time = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.task

# Create your models here.
