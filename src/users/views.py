from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
			
	else:
		messages.error(request, f'Incorrect format. Please try again.')
		form = UserRegisterForm()
		return render(request, 'register.html', {'form': form})