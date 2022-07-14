from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages
from django.contrib.auth.models import auth,User
# Create your views here.

def home(request):
	items = Item.objects.all()
	return render(request, 'home.html', {'items':items})

def signup(request):

	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password1 = request.POST['password1']

		if password == password1:
			if User.objects.filter(username=username).exists():
				messages.info(request, "Username exists")
				return redirect('signup')
			elif User.objects.filter(email=email).exists():
				messages.info(request, "email taken")
				return redirect('signup')
			else:
				user = User.objects.create_user(username=username,email=email,password=password)
				user.save();
				return redirect('login')
		else:
			messages.info(request, 'Unmatching password')
			return redirect('signup')
	else:
		return render(request, 'signup.html')		

def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request, 'Invalid credentials')
			return redirect('login')
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def displayItem(request, pk):
	item = Item.objects.get(id=pk)
	return render(request, 'displayItem.html', {'item':item})


	

