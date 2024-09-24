from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AdminProfile, FundTransfer
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import AdminRegisterProfile, AddFundsForm, WithdrawFundsForm, TransferFundsForm
from django.contrib.auth.decorators import user_passes_test

def register_user(request):
    if request.method == 'POST':
        form = AdminRegisterProfile(request.POST)
        if form.is_valid():
            form.save()  # Save user and profile
            return redirect('admin_dashboard')  # Redirect to the dashboard after success
    else:
        form = AdminRegisterProfile()

    return render(request, 'register_user.html', {'form': form})


def admin_dashboard(request):
    # Get all users and their corresponding profile information (balance)
    users = User.objects.all().select_related('adminprofile')
    return render(request, 'admin_dashboard.html', {'users': users})

# Only allow access if the user is an admin
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.all().select_related('adminprofile')
    return render(request, 'admin_dashboard.html', {'users': users})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("apple", user)
        if user is not None:
            login(request, user)
            return redirect('user_home')
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def user_home(request):
    # Fetch the user's profile
    admin_profile = AdminProfile.objects.get(user=request.user)
    total_balance = admin_profile.balance  # Get the balance
    return render(request, 'user_home.html', {'total_balance': total_balance})


@login_required
def transfer_funds(request):
    if request.method == 'POST':
        sender = AdminProfile.objects.get(user=request.user)
        users = User.objects.exclude(username=request.user.username)
        amount = float(request.POST['amount'])
        
        try:
            recipient = AdminProfile.objects.get(user__username=users)
            if sender == recipient:
                messages.error(request, "You cannot transfer money to yourself.")
            else:
                transfer = FundTransfer(sender=sender, recipient=recipient, amount=amount)
                transfer.save()
                messages.success(request, f"Successfully transferred {amount} to {recipient.user.username}.")
        except AdminProfile.DoesNotExist:
            messages.error(request, "Recipient not found.")
    return render(request, 'transfer.html')



