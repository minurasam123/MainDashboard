from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def admin(request):
    return render(request,'General/general.html')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'General/SignUpPage.html', context)

def loginPage(request):

    context = {}
    return render(request, 'General/Login page.html', context)
