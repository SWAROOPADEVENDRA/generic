from django.shortcuts import render

# Create your views here.
def biriyani(request):
    return render(request,'biriyani.html')


def chicken(request):
    return render(request,'chicken.html')