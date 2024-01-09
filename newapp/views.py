

from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Spot

# Create your views here.


def new(request):
    obj=Place.objects.all()
    obj1=Spot.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# def demo(request):
#     obj=Spot.objects.all()
#     return render(request,"index.html",{'result':obj})

#def about(request):
  #  return render(request,"about.html")
#def contact(request):
 #   return render(request,"contact.html")
#def detail(request):
   # return HttpResponse("my detail")
