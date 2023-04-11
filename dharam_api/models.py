from django.db import models

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



