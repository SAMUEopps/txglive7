from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Reg_fee 


# Create your views here.
def index(request):
	return render(request, 'cashbag/index.html')	

def register(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')
	context = {'form':form}		
	return render(request, 'cashbag/register.html', context)

def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('reg_fee')
			
	return render(request, 'cashbag/login.html',)	

def dashboard(request):
	code = Profile.objects.all()
	context = {'code':code}
	return render(request, 'cashbag/dashboard.html', context)

def reg_fee(request):
	if request.method == 'POST':
		if request.POST.get('username') and request.POST.get('mpesa_code') and request.POST.get('full_names'):
			reg_fee=Reg_fee()
			reg_fee.username= request.POST.get('username')
			reg_fee.mpesa_code= request.POST.get('mpesa_code')
			reg_fee.full_names= request.POST.get('full_names')
			reg_fee.save()
		return redirect('dashboard')   
	return render(request, 'cashbag/reg_fee.html')

#def investment(request):
#	if request.method == 'POST':
#		if request.POST.get('username') and request.POST.get('mpesa_code') and request.POST.get('full_names'):
#			deposit=Deposit()
#			deposit.username= request.POST.get('username')
#			deposit.mpesa_code= request.POST.get('mpesa_code')
#			deposit.full_name= request.POST.get('full_name')
#			deposit.save()
#		return redirect('dashboard')   
#	return render(request, 'cashbag/investment.html')

def navbar(request):
	return render(request, 'cashbag/navbar.html')

def my_recommendations_view(request):
	profile = Profile.objects.get(user=request.user)
	my_recs = profile.get_recomended_profiles()
	context = {'my_recs':my_recs}
	return render(request, 'cashbag/dashboard.html', context)


