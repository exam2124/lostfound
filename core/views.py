# core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   # protects pages
from django.contrib import messages
from .models import Item


# ══════════════════════════════════════════════════════════════════
#  SIGNUP VIEW — New users create an account here
# ══════════════════════════════════════════════════════════════════
def signup_view(request):
    if request.method == 'POST':
        username         = request.POST['username']
        email            = request.POST['email']
        password         = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check username is not already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Try another.")
            return redirect('signup')

        # Create the new user and save to database
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    # GET request — just show the signup form
    return render(request, 'core/signup.html')


# ══════════════════════════════════════════════════════════════════
#  LOGIN VIEW — Existing users sign in here
# ══════════════════════════════════════════════════════════════════
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate() checks username + password against the database
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)          # creates a session
            return redirect('home')       # go to dashboard
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'core/login.html')


# ══════════════════════════════════════════════════════════════════
#  LOGOUT VIEW — Signs the user out
# ══════════════════════════════════════════════════════════════════
def logout_view(request):
    logout(request)
    return redirect('login')


# ══════════════════════════════════════════════════════════════════
#  HOME VIEW — Main dashboard (requires login)
# ══════════════════════════════════════════════════════════════════
@login_required   # if not logged in, redirects to /login/
def home_view(request):
    if request.method == 'POST':
        # Get form values from the popup
        item_type    = request.POST.get('item_type')   # 'lost' or 'found'
        item_name    = request.POST.get('item_name')
        description  = request.POST.get('description')
        location     = request.POST.get('location')
        date_time    = request.POST.get('date_time')
        contact_info = request.POST.get('contact_info', '')
        image        = request.FILES.get('image')      # uploaded file

        # Save the item to the database
        Item.objects.create(
            user         = request.user,
            item_type    = item_type,
            item_name    = item_name,
            description  = description,
            location     = location,
            date_time    = date_time,
            contact_info = contact_info,
            image        = image,
        )

        label = "Lost" if item_type == 'lost' else "Found"
        messages.success(request, f"{label} item '{item_name}' reported successfully!")
        return redirect('home')

    return render(request, 'core/home.html')


# ══════════════════════════════════════════════════════════════════
#  ITEMS VIEW — Shows all items reported by all users
# ══════════════════════════════════════════════════════════════════
@login_required
def items_view(request):
    # Filter by type, newest first
    lost_items  = Item.objects.filter(
        item_type='lost'
    ).order_by('-reported_at')

    found_items = Item.objects.filter(
        item_type='found'
    ).order_by('-reported_at')

    return render(request, 'core/items.html', {
        'lost_items':  lost_items,
        'found_items': found_items,
    })