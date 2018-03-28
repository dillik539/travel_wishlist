from django.db import models
from django.utils import timezone

# Create your models here.

'''a place model added with max length of 200, a default of False to visited variable
a dateTimeField with current time as default and text field to hold text content'''
class Place(models.Model):
    name = models.CharField(max_length = 200)
    visited = models.BooleanField(default = False)
    date_visited = models.DateTimeField(default = timezone.now)
    comment = models.TextField()


    def __str__(self):
        return '%s visited? %s %s %s' % (self.name, self.visited, self.date_visited, self.comment)
