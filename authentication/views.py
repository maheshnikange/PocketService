from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import UserForm
from admin_panel.models import Advertise

# Create your views here.



def login(request):
    print("Login---------------------auth")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )
        if user is not None:
            auth.login(request , user)
            if user.role == 'vendor':
                return redirect('vendor_dashboard')  
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        advertise_images = Advertise.objects.filter(location='dashboard')
        return render(request,'index.html', {"advertise_images": advertise_images})

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('user_login')


def register(request):
    form = UserForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('login_page')
    return redirect('register_page')