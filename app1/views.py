from django.shortcuts import render
from app1.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def displaytopics(request):
    topics=Topic.objects.all()

    d={'topics':topics}
    return render (request,'displaytopics.html',d)




def updatemethod(request):
    Webpage.objects.filter(name='fe').delete()
    LWO=Webpage.objects.all().delete()
    d={'LWO':LWO}
    return render (request,'updatemethod.html',d)


def webpages(request):
    
    LWO=Webpage.objects.all()
    #LWO=Webpage.objects.filter(topic_name='jan')
    #LWO= Webpage .objects.all()[::-1]
    #LWO= Webpage .objects.all().order_by('-name')
    #LWO= Webpage .objects.all()[3::]
    #LWO=Webpage.objects.exclude(topic_name='jan')
    #LWO=Webpage.objects.filter(name__startswith='j')
    #LWO=Webpage.objects.filter(name__endswith='k')
    #LWO=Webpage.objects.all().order_by(Length('name').desc())
    #LWO=Webpage.objects.filter(name__contains='m')
    #LWO=Webpage.objects.filter(name__in=['fe','ma'])
    #LWO=Webpage.objects.filter(name__regex='r\wf+')
    #LWO=Webpage.objects.filter(Q(name='fe')|Q(url__startswith='http'))
    #LWO=Webpage.objects.filter(Q(name='fe')&Q(url__startswith='http'))
    
    
    d={'LWO':LWO}
    return render(request,'webpages.html',d)

def access(request):
    LAO=AccessRecords.objects.all()
    #LAO=AccessRecords.objects.filter(date='2023-06-30')
    #LAO=AccessRecords.objects.filter(date__gt='2020-08-08')
    #LAO=AccessRecords.objects.filter(date__lt='2020-08-08')
    #LAO=AccessRecords.objects.filter(date__gte='2020-08-08')
    # LAO=AccessRecords.objects.filter(date__lte='2020-08-08')
    #LAO=AccessRecords.objects.filter(date__year__gt='2020')
    #LAO=AccessRecords.objects.filter(date__month__gte='08')
    #LAO=AccessRecords.objects.filter(date__day__gte='06')

    d={'LAO':LAO}
    
    
    return render(request,'access.html',d)
