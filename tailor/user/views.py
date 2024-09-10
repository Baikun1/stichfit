from django.shortcuts import render
from django.http import HttpResponse
# user/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        # Extract data from the form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        # Generate user_id (combination of first name, phone number, and zip code)
        user_id = f"{first_name}{phone_number}{zip_code}"
        print(user_id)

        # Check if a user with this email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'user/signin.html', {'error': 'Email already exists.'})

        # Create new User object
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code
        )

        # Save the User object to the database
        new_user.save()

        # Display a success message and redirect to a success page
        messages.success(request, 'User registered successfully.')
        return redirect('home/index.html')  # Replace 'home' with the URL name of the home page

    return render(request, 'user/signin.html')


# Create your views here.
def user(request):
    return HttpResponse('hi ths is user')