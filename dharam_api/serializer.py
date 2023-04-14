from django.contrib.auth.models import User, Group
from rest_framework import serializers
from dharam_api.models import User_details,feedback,Invoice,History



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']




class User_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_details
        fields = ['name','username','password','mobile','email','select_id','id_number','otp','otp_verify']        
        # fields = ['username','password']        



class feedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = feedback
        fields = ['userfeedback', 'user_id','date']



class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['mobile_number','date','customer_name','customer_email','total_amount']      



class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'date', 'location', 'status', 'time', 'accepted')
