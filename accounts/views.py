from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib import messages
from .models import *
from .forms import CommentForm, CreateCustomerForm, CustomerProfileForm, OrderForm, ReservationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .decorators import allowed_users, unauthenticated_user

# Create your views here.

@login_required(login_url='userLogin')
@allowed_users(2)
def home(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer)
    reservations = Reservation.objects.filter(customer=customer)
    context = {'orders' : orders, 'reservations' : reservations}
    return render(request, 'accounts/home.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def comment(request, pk):
    restaurant = Restaurant.objects.get(user_id=pk)
    comments = Comment.objects.filter(res=restaurant)
    customer = request.user.customer
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(cust = customer, res=restaurant)
            messages.success(request, 'Comment succesfully created!')
            strId = str(restaurant.user_id)
            return redirect('/comment/' + strId)
		
    context = {'form':form, 'res' : restaurant, 'comments' : comments}
    return render(request, 'accounts/comment.html', context)


    


@login_required(login_url='userLogin')
@allowed_users(2)
def restaurants(request):
    restaurants = Restaurant.objects.all()
    context = {"restaurants" : restaurants}    
    return render(request, 'accounts/restaurants.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def cancel_res(request, pk):
    reservation = Reservation.objects.get(id=pk)
    reservation.delete()
    messages.success(request, 'Reservation is deleted successully!')
    return redirect('/')

@login_required(login_url='userLogin')
@allowed_users(2)
def cancel_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    messages.success(request, 'Order is deleted successully!')
    return redirect('/')

    

@login_required(login_url='userLogin')
@allowed_users(2)
def search(request):
    context = {} 
    return render(request, 'accounts/search.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def order(request, pk):
    restaurant = Restaurant.objects.get(user_id=pk)
    menu = Menu.objects.get(res = restaurant)
    items = MenuElement.objects.filter(menu = menu)
    form = OrderForm()
    customer = request.user.customer
    res = restaurant
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(cust = customer, res=res)
            messages.success(request, 'Order succesfully created!')

            return redirect('home')
		
    context = {'form':form, 'menu':items}
    return render(request, 'accounts/order.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def order_details(request, pk):
    order = Order.objects.get(id=pk)
    customer =  order.customer
    res = order.res
    status = False
    if order.status != "Restaurant Declined" and order.status != "Done":
        status = True
    context = {'order' : order, 'res' : res, 'status' : status}
    return render(request, 'accounts/order_details.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def reservation(request, pk):
    restaurant = Restaurant.objects.get(user_id=pk)
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        res = restaurant
        customer = request.user.customer
        if form.is_valid():
            form.save(cust = customer, res = res)

            messages.success(request, 'Reservation succesfully created!')

            return redirect('home')
		

    context = {'form':form}
    return render(request, 'accounts/reservation.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def reservation_details(request, pk):
    reservation = Reservation.objects.get(id=pk)
    customer =  reservation.customer
    res = reservation.res
    status = False
    if reservation.status != "Restaurant Declined" and reservation.status != "Done":
        status = True
    context = {'reservation' : reservation, 'res' : res, 'status' : status}
    return render(request, 'accounts/reservation_details.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def profile(request):
    customer = request.user.customer
    form  = CustomerProfileForm(instance=customer)
    context = {'form' : form} 
    return render(request, 'accounts/profile.html', context)

@unauthenticated_user
def userRegister(request):
    form = CreateCustomerForm()

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + user + ' succesfully!')
            return redirect('userLogin')

    context = {'form': form} 
    return render(request, 'accounts/userRegister.html', context)

@unauthenticated_user
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User or password is incorrect!')

    context = {} 
    return render(request, 'accounts/userLogin.html', context)

@login_required(login_url='userLogin')
@allowed_users(2)
def logoutUser(request):
    logout(request)
    return redirect('userLogin')

unauthenticated_user
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password_reset_email.txt"
					c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})