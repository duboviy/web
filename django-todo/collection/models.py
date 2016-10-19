from __future__ import unicode_literals

from django.db import models


class todo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField()
 
    def __unicode__(self):
        return self.name

    __str__ = __unicode__
