from django.db import models


class DepartmentManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Department(models.Model):
    objects = DepartmentManager()

    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

    def natural_key(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    __str__ = __unicode__
