# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
import json
from models import *

#from incidents.models import Incident, CrimeKey




def index(request):
    latest_incident_list = Incident.objects.order_by('-date')[:10].values('offense__category','address','id','caseno','date','offense','ward','lat','long')
    #latest_incident_data = serializers.serialize("json", Incident.objects.order_by('-date')[:10].values('offense__category','address','id','caseno','date','offense','ward','lat','long'))
    context = {'latest_incident_list': latest_incident_list}
    return render(request, 'incidents/index.html', context)

def details(request, id):
    try:
        incident = Incident.objects.values('offense__category','address','id','caseno','date','offense','ward','lat','long').get(pk=id)
    except Incident.DoesNotExist:
        raise Http404
    return render(request, 'incidents/detail.html', {'incident': incident})

def offense(request, offense):
    latest_offense_list = []
    big_offense_list = Incident.objects.order_by('-date')[:1000].values('offense__category','address','id','caseno','date','offense','ward','lat','long')
    for thing in big_offense_list:
        if thing['offense__category'] == offense:
            latest_offense_list.append(thing)
    #latest_offense_list = [x for x in big_offense_list if x == x.offense__category]
    context = {'latest_offense_list': latest_offense_list}
    return render(request, 'incidents/offense.html', context)

def offenselist(request):
    return HttpResponse("This is where offense list lives")

def map(request):
    data = [incident.json() for incident in Incident.objects.all().order_by('-date')[:1000].values('offense__category','address','id','caseno','date','offense','ward','lat','long')]
    #data = [incident['offense__category'] for incident in Incident.objects.all().order_by('-date')[:1000].values('offense__category','address','id','caseno','date','offense','ward','lat','long')]
    return HttpResponse(json.dumps(data), content_type='application/json')












