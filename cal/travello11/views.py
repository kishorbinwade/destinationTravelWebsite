from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    dests= destination.objects.all()


    #return render(request,"index.html",{'dest1':dest1,'dest2':dest2,'dest3':dest3} )
    return render(request,"index.html",{'dests':dests})