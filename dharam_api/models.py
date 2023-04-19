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






class History(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255) 
    time = models.TimeField()
    accepted = models.BooleanField(default=False)




class Notications(models.Model):
    accepted = models.CharField(max_length=255)
    posted = models.CharField(max_length=255)
    date = models.DateTimeField()    

    # accepted = models.BooleanField(default=False)
    # posted = models.BooleanField(default=False)
    # date = models.DateTimeField(auto_now_add=True)
    # 
   
class User_Settings(models.Model):
    select_Hospital= models.CharField(max_length=255, null=True)  
    emergency_number = models.CharField(max_length=20,null=True) 
    whatsapp_number = models.CharField(max_length=20,null=True ) #whatsapp
    Notications_on=models.BooleanField(null=True)
