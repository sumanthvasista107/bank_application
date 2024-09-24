from django import forms
from django.contrib.auth.models import User
from .models import AdminProfile

class AdminRegisterProfile(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    balance = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = AdminProfile
        fields = ['username', 'email', 'password', 'balance']

    def save(self, commit=True):
        # First, create the user
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        # Then create the profile with the balance
        profile = AdminProfile(user=user, balance=self.cleaned_data['balance'])
        if commit:
            profile.save()
        return profile
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance'].initial = 10000
    
class AddFundsForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class WithdrawFundsForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class TransferFundsForm(forms.Form):
    recipient_username = forms.CharField(max_length=150)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
