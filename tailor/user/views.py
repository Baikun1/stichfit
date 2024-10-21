from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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

        # Validate that all fields are provided
        if not all([first_name, last_name, email, password, phone_number, address, city, state, zip_code]):
            messages.error(request, 'All fields are required.')
            return render(request, 'user/signin.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'user/signin.html')

        # Create a new user
        new_user = User(
            username=email.split('@')[0],  # Use email prefix as username
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        new_user.set_password(password)  # Set the password
        new_user.save()

        # Store additional fields in the User instance
        new_user.phone_number = phone_number
        new_user.address = address
        new_user.city = city
        new_user.state = state
        new_user.zip_code = zip_code
        new_user.save()

        messages.success(request, 'User  registered successfully.')
        return redirect('index')  # Redirect to a named URL

    return render(request, 'user/signin.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate using the username (derived from email)
        user = authenticate(request, username=email.split('@')[0], password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return render(request, 'index.html')  # Redirect to a named URL
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'user/login.html')

    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'user/login.html')  # Redirect to the login page after logout

def profile(request):
    return HttpResponse('Hi, this is the user page.')