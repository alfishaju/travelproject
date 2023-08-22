
from django.shortcuts import render
from .models import place, world, travel, person


# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=world.objects.all()
    obj2=travel.objects.all()
    obj3=person.objects.all()

    return render(request,'index.html',{'result':obj,'result1':obj1,'result2':obj2,'result3':obj3})




