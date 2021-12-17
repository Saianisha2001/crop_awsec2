from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def index(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ProfileForm()

	img = Profile.objects.all().order_by('-date_posted')
	return render(request, 'user/home.html', {'form':form, 'img':img})
