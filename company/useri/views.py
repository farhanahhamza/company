from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user profile
            return redirect('success_page')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'Registrationpage.html', {'form': form})

def success_page(request):
    if request.method=="GET":
        return render(request,'Success_page.html')
    
def course_showcase(request):
    if request.method=="GET":
        return render(request,'Course_show.html')
    
def soft(request):
    if request.method=="GET":
        return render(request,'st.html')
    
def mearn(request):
    if request.method=='GET':
        return render (request ,'Mearn.html' )
    
def data(request):
    if request.method=="GET":
        return render(request ,"Data.html")
    
def python(request):
    if request.method=="GET":
        return render(request ,"Python.html")
    
def asp(request):
    if request.method=="GET":
        return render(request ,"Asp.html")
    
def android(request):
    if request.method=="GET":
        return render(request ,"Android.html")
    
def ds(request):
    if request.method=="GET":
        return render(request ,"Ds.html")
    
def ds(request):
    if request.method=="GET":
        return render(request ,"Ds.html")
    
def java(request):
    if request.method=="GET":
        return render(request,"Java.html" )