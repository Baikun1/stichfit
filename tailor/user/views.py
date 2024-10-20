from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def signin(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        if not all([first_name, last_name, email, password, phone_number, address, city, state, zip_code]):
            messages.error(request, 'All fields are required.')
            return render(request, 'user/signin.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'user/signin.html')

        user_id = f"{first_name}{phone_number}{zip_code}"
        print(user_id) 

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code
        )
        new_user.set_password(password)

        new_user.save()

        messages.success(request, 'User registered successfully.')
        return render(request,'index.html')

    return render(request, 'user/signin.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return render(request,'index.html')  
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'user/login.html') 

    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')


def profile(request):
    return HttpResponse('Hi, this is the user page.')
