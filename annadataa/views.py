from django.shortcuts import render



# Create your views here.
def home(request):
    
    return render(request, 'annadataa/home.html', {})

def ngo(request):
    return render(request, 'annadataa/ngo.html')