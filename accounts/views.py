from .forms import ordersform,CreateUserForm,CreateCustomer1
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
def registerpage1(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created.' + user)
			return redirect('login')
	context = {'form':form}
	return render(request,'accounts/registerpage.html',context)
def loginpage(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username, password=password)
		if user is not None:
			auth_login(request,user)
			return redirect('/')
		else:
			messages.info(request,'username OR password is incorrect')
			

	return render(request,'accounts/loginpage.html')
def logoutuser(request):
	logout(request)
	return redirect('login')




#@ login_required(login_url='login')
def home (request):
	ord = orders.objects.all()
	cust = customer.objects.all() 
	#total_customers = customer.count()
	total_orders = orders.objects.count()
	delivered1 = orders.objects.filter(status="Delivered").count()
	pending1 = orders.objects.filter(status="Pending").count()
	context = {'ord':ord, 'cust':cust, 'total_orders':total_orders, 'delivered1':delivered1, 'pending1':pending1}
	return render(request,'accounts/dashboard.html',context)
def products1(request):
	trs = products.objects.all()
	#values = {'first':trs}
	return render(request,'accounts/products.html',{'trs':trs})
def customers1(request):
	customer1 = customer.objects.all()
	order = customer1.all().order_by('-id')
	context = {'customer1':customer1, 'order':order}
	return render(request,'accounts/customers.html',context)

@login_required(login_url='login')

def createorder(request):
	#import pdb;pdb.set_trace()
	form = ordersform()
	if request.method == "POST":
		form = ordersform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request,'accounts/order_form.html',context)

@login_required(login_url='login')

def update_order(request,pk):
	order1 = orders.objects.get(id=pk)
	form = ordersform(instance=order1)
	if request.method == "POST":
		form = ordersform(request.POST, instance=order1)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request,'accounts/order_form.html',context)

@login_required(login_url='login')

def createcustomer(request):
	# import pdb;pdb.set_trace()
	form = CreateCustomer1()
	if request.method =="POST":
		form =  CreateCustomer1(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request,'accounts/createcostomer_form.html',context)		


