from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

COLORS_CHOICE = (
    ('Visa', 'Visa Card'),
    ('Master', 'Master Card'),
)

STATUS =(
    ('Pending', 'Pending'),
    ('Declined', 'Declined'),
    ('Approved', 'Approved'),
)

CARD_DIF =(
    ('Debit Card', 'Debit'),
    ('Credit Card', 'Credit'),
)



class Cards(models.Model):
    card_id = models.UUIDField(default=uuid.uuid4)
    account_holder = models.CharField(max_length=30)
    card_number = models.CharField(max_length=12)
    cvv = models.IntegerField()
    price = models.FloatField()
<<<<<<< HEAD
    card_limit = models.CharField(max_length=30, null=True)
=======
    duration = models.CharField(max_length=30)
>>>>>>> 9100fb1981374a5ae0fafe6285764df628d30dda
    card_type = models.CharField(choices=COLORS_CHOICE, max_length=8)
    card_dif = models.CharField(choices=CARD_DIF, max_length=12, null=True)

    def __str__(self):
        return self.account_holder

    class Meta:
        verbose_name_plural = 'Card'



class Payment_screenshot(models.Model):
    user = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    sent_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Screenshots", null=True)

    def __str__(self):
        return f"{self.user} sent {self.image} on {self.sent_on}"

    class Meta:
        verbose_name_plural = 'Payment_screenshots'



class User_orders(models.Model):
    user = models.CharField(max_length=100)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)
    order_status = models.CharField(choices=STATUS, max_length=8, default="Pending", null=True)
    transaction_type = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = 'Orders'
