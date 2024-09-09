from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was successfully created.")
            
            # Authenticate the user using the username (or email if configured)
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            
            if new_user is not None:
                login(request, new_user)
                return redirect("core:index")
            else:
                messages.error(request, "Authentication failed.")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/signup.html", context=context)
