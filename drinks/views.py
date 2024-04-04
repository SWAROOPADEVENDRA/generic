from django.shortcuts import render

# Create your views here.
def apple(request):
    return render(request,'apple.html')

def pine_apple(request):
    return render(request,'pine_apple.html')