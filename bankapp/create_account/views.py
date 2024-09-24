from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AdminProfile, Transaction
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import AdminRegisterProfile, AddFundsForm, WithdrawFundsForm, TransferFundsForm
from django.contrib.auth.decorators import user_passes_test

def register_user(request):
    if request.method == 'POST':
        form = AdminRegisterProfile(request.POST)
        if form.is_valid():
            form.save()  # Save user and profile
            print("apple")
            return redirect('admin_dashboard')  # Redirect to the dashboard after success
    else:
        form = AdminRegisterProfile()

    return render(request, 'register_user.html', {'form': form})

# Only allow access if the user is an admin
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.all().select_related('adminprofile')
    return render(request, 'admin_dashboard.html', {'users': users})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Check if the user is a superuser
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirect to the admin dashboard
            else:
                return redirect('user_home')  # Redirect to the user home page for regular users
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')  # Render the login page

@login_required
def user_home(request):
    # Fetch the user's profile
    admin_profile = AdminProfile.objects.get(user=request.user)
    total_balance = admin_profile.balance  # Get the balance
    return render(request, 'user_home.html', {'total_balance': total_balance})


from decimal import Decimal

@login_required
def transfer_funds(request):
    if request.method == 'POST':
        recipient_username = request.POST['recipient_username']
        amount = Decimal(request.POST['amount'])
        sender_profile = AdminProfile.objects.get(user=request.user)

        try:
            recipient_user = User.objects.get(username=recipient_username)
            recipient_profile = AdminProfile.objects.get(user=recipient_user)

            if sender_profile.balance >= amount:
                # Deduct amount from sender
                sender_profile.balance -= amount
                sender_profile.save()

                # Add amount to recipient
                recipient_profile.balance += amount
                recipient_profile.save()

                # Create a transaction record
                transaction = Transaction(sender=request.user, recipient=recipient_user, amount=amount)
                transaction.save()

                # Success message
                messages.success(request, f"Successfully transferred {amount} to {recipient_username}.")

            else:
                messages.error(request, "Insufficient balance.")

        except User.DoesNotExist:
            messages.error(request, "Recipient not found.")

    sender_profile = AdminProfile.objects.get(user=request.user)  # Get the latest balance
    return render(request, 'transfer.html', {'balance': sender_profile.balance})

