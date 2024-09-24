
from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default="default@example.com")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.user.username
    
class Account(models.Model):
    user = models


class FundTransfer(models.Model):
    sender = models.ForeignKey(AdminProfile, on_delete=models.CASCADE, related_name='sent_transfers')
    recipient = models.ForeignKey(AdminProfile, on_delete=models.CASCADE, related_name='received_transfers')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.sender.balance >= self.amount:  # Ensure sender has enough balance
            self.sender.balance -= self.amount
            self.recipient.balance += self.amount
            self.sender.save()
            self.recipient.save()
            super(FundTransfer, self).save(*args, **kwargs)
        else:
            raise ValueError("Insufficient balance")

    def __str__(self):
        return f"{self.sender.user.username} transferred {self.amount} to {self.recipient.user.username}"

