from django.db import models

# Create your models here.

class CrimeKey(models.Model):
    offense = models.CharField(max_length=200,blank=True,unique=True)
    category = models.CharField(max_length=200)

    def json(self):
        return {
            'offense': self.offense,
            'category': self.category,
            'incidents': [incident.json() for incident in Incident.objects.all().order_by('-date')]
        }
	
    def __unicode__(self):
        return self.category

class Incident(models.Model):
    address = models.CharField(max_length=200,blank=True)
    caseno = models.CharField(max_length=200,blank=True)
    date = models.DateTimeField('date and time occured')
    offense = models.ForeignKey(CrimeKey, to_field="offense")
    ward = models.CharField(max_length=200,blank=True)
    lat = models.FloatField(blank=True)
    long = models.FloatField(blank=True)

    def json(self):
        fields = ('address', 'caseno', 'date', 'offense__category', 'offense', 'ward', 'lat', 'long')
        return dict((field, self.__dict__[field]) for field in fields)

    def __unicode__(self):
        return self.offense
