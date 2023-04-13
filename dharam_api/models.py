from django.db import models
import datetime

class User_details(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    select_id = models.IntegerField()
    id_number = models.CharField(max_length=255)
    otp= models.IntegerField(default=0)
    otp_verify= models.BooleanField(default=False)



class feedback(models.Model):
    userfeedback = models.CharField(max_length=255)
    user_id = models.ForeignKey(User_details, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)



class Invoice(models.Model):
    mobile_number = models.CharField(max_length=20)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)  
    customer_email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
