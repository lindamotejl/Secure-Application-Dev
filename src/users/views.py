from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')     
			return redirect('login')
	else:
		form = UserRegisterForm()
		return render(request, 'register.html', {'form': form})