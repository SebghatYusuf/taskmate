from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegisterForm


def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Registeration Success! Login to access.'))
            return redirect('register')
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {"form": form})
