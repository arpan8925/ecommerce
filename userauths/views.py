from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from userauths.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            messages.success(request, f"Hey {username}, your account was successfully created.")

            login(request, new_user)
            return redirect("core:index")
        else:
            messages.error(request, "There was a problem with your registration details.")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/signup.html", context=context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect("core:index")
            else:
                messages.warning(request, "Please create an account")
        except:
            messages.warning(request, f"User with {email} does not exist")


    context = {
    }
    
    return render(request, "userauths/signin.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect("userauths:signin")