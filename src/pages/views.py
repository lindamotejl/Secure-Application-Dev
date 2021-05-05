from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def results_view(request):
    return render(request, "results.html", {})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home.html')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
