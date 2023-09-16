from django.shortcuts import render,redirect,HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from.forms import Aforms
from .models import Amodel

# Create your views here.


def home(request):
    if request.method=="GET":
        return render(request,"Home.html")
    
def main(request):
    if request.method=="GET":
        return render(request,'Main.html')
    
def signin(request):
    if request.method=="POST":
        Username = request.POST['Username']
        Password = request.POST['Password']

        user=authenticate(Username=Username,Password=Password)

        if user is not None:
            signin(request,user)
            return HttpResponse("login")
        else:
            return redirect('signin')
    return render(request,'Signin.html')
    
def signup(request):
    if request.method=="POST":
        Email = request.POST['Email']
        Username = request.POST['Username']
        Password = request.POST['Password']

        myuser=User.objects.create_user(Email,Username,Password)
        myuser.save()

        return redirect('signin')
    
    return render(request,'Signup.html')
    
# def register(request):
#         if request.method == 'POST':
#             form = RegistrationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('login')  # Redirect to the login page after successful registration
#         else:
#             form = RegistrationForm()
#         return render(request, 'Registrationpage.html')
    
def course(request):
    if request.method=="POST":
        fm=Aforms(request.POST)
        if fm.is_valid():
            fm.save()
        fm=Aforms()
    else:
            fm=Aforms()
    stu=Amodel.objects.all()
    return render(request,'course.html',{'fm':fm , 'stu':stu})
