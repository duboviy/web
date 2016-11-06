from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    PRIORITY_CHOICES = (
        (0, 'High'),
        (1, 'Medium'),
        (2, 'Low'),
    )
    title = models.CharField(max_length=20, blank=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['priority']
