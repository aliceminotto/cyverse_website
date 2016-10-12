from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator


@python_2_unicode_compatible
class Application(models.Model):
    name=models.CharField(max_length=200)
    version=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    more=models.TextField()
    uri=models.CharField(max_length=200)

    def __str__(self):
        return self.name()+" "+self.version()

class Input(models.Model):
    app=models.ForeignKey(Application, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    requirement=models.BooleanField(default=False)
    value=models.CharField(max_length=200)
    label=models.CharField(max_length=200)
    max_values=models.IntegerField(default=1)

    def __str__(self):
        return self.name()+ " "+self.label()

class Parameter(models.Model):
    app=models.ForeignKey(Application, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    visibility=models.BooleanField(default=True)
    label=models.CharField(max_length=200)
    re_validation="" ####here the validator expression from the json
    #type_accepted=RegexValidator(regex=self.re_validation, message="the given value for %s is not valid." % self.name, code=None, inverse_match=None, flags=0)
    value="" ######i think this depends on type_accepted
    max_values=models.IntegerField(default=1)

    def __str__(self):
        return self.name()+" "+self.label()
