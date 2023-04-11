from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from dharam_api.serializer import  GroupSerializer,User_detailsSerializer 
from dharam_api.models import User_details

from rest_framework import generics, permissions
from rest_framework.response import Response
# from dharam_api.models import AuthToken
from dharam_api.serializer import UserSerializer
import json
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
import math, random


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class User_detailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User_details.objects.all()
    serializer_class = User_detailsSerializer
    permission_classes = [permissions.IsAuthenticated]    

    

class SignupView(GenericAPIView):
    serializer_class = User_detailsSerializer
    
    def post(self, request, *args, **kwargs):
        print(request)
        otp = otpView.get(self, request)
        print(otp.content.decode())
        response = {
            'massege': "signup succefully",
            'data' : json.loads(self.request.body.decode()),
            'otp' : otp.content.decode()
        }
        print(json.dumps(response, indent=4))

        return HttpResponse(json.dumps(response, indent=4))

    
    def get(self, request, *args, **kwargs):
        print(self.request.body)
        user_data_json = json.loads(self.request.body)
        print(user_data_json["username"])
        try:
            user_fetch_data = User_details.objects.get(username=user_data_json["username"])
        except:
            return HttpResponse("Invalide username password")
    
        # for i in user_fetch_data:
        #     print(i)
        if user_fetch_data:
            print(user_fetch_data.username)
            if user_fetch_data.username == user_data_json["username"] and user_fetch_data.password ==  user_data_json["password"]:
                return HttpResponse(self.request.body)
            else:
                return HttpResponse("Login unsuccefully")
        else:
            return HttpResponse("Login unsuccefully")
        

class LoginView(GenericAPIView):
    serializer_class = User_detailsSerializer
    
    
    def get(self, request, *args, **kwargs):
        print(self.request.body)
        user_data_json = json.loads(self.request.body)
        print(user_data_json["username"])
        try:
            user_fetch_data = User_details.objects.get(username=user_data_json["username"])
        except:
            return HttpResponse("Invalide username password")
    
        # for i in user_fetch_data:
        #     print(i)
        if user_fetch_data:
            print(user_fetch_data.username)
            if user_fetch_data.username == user_data_json["username"] and user_fetch_data.password ==  user_data_json["password"]:
                return HttpResponse(self.request.body)
            else:
                return HttpResponse("Login unsuccefully")
        else:
            return HttpResponse("Login unsuccefully")
        
class otpView(GenericAPIView): 
# function to generate OTP
    def get(self, request, *args, **kwargs):
    
        # Declare a digits variable 
        # which stores all digits
        digits = "0123456789"
        OTP = ""
    
    # length of password can be changed
    # by changing value in range
        for i in range(6) :
            OTP += digits[math.floor(random.random() * 10)]
     
        return HttpResponse(OTP)
 
class resetpasswordView(GenericAPIView): 
    def patch(self, request, *args, **kwargs):
        email = json.loads(self.request.body.decode())['email']
        print(email)
        check_email = User_details.objects.get(email=email)
        if check_email:
            if json.loads(self.request.body.decode())['password'] :
                check_email.password = json.loads(self.request.body.decode())['password']
         
                response = {
                'massege': "password update successfully",
                }
                print(json.dumps(response, indent=4))
                return HttpResponse((json.dumps(response, indent=4)))
            else:
                HttpResponse("Password1 and Password2 is not matched")
        else:
            return HttpResponse("Email Not found")



class forgotpassword(GenericAPIView):
    def post(self, request, *args, **kwargs):
        print(request)
        otp = otpView.get(self, request)
        print(otp.content.decode())
        response = {
            'massege': "signup succefully",
            'data' : json.loads(self.request.body.decode()),
            'otp' : otp.content.decode()
        }
        print(json.dumps(response, indent=4))

       
        return HttpResponse(json.dumps(response, indent=4))
    def post(self, request, *args, **kwargs):
        print(request)
        otp = otpView.get(self, request)
        print(otp.content.decode())
        response = {
            'massege': "signup succefully",
            'data' : json.loads(self.request.body.decode()),
            'otp' : otp.content.decode()
        }
        print(json.dumps(response, indent=4))

        return HttpResponse(json.dumps(response, indent=4))

class forgotpassword(GenericAPIView):
    def post(self, request, *args, **kwargs):
        mobile = json.loads(self.request.body.decode()) ["mobile"]
        user_data = User_details.objects.get(mobile=mobile)
        if user_data.mobile : 
            otp=otpView.get(self,request).content.decode()
            user_data.otp = int(otp)
            user_data.save()
            response = {
            'massege': "otp send succefully",
            'otp' : otp
            
            }
            return HttpResponse(json.dumps(response, indent=4))
        else:
            return HttpResponse("Invalide mobile number")


class otpverify(GenericAPIView):
    def post(self, request, *args, **kwargs):
        mobile = json.loads(self.request.body.decode()) ["mobile"]
        
        otp = json.loads(self.request.body.decode()) ["otp"]


        user_data = User_details.objects.get(mobile=mobile)
        if user_data.mobile : 
            if user_data.otp==otp:
             user_data.otp_verify=True
             user_data.save()
             response = {
               'massege': "otp verify succefully",
               }
             return HttpResponse(json.dumps(response, indent=4))
            else:
                return HttpResponse("otp number not verify")

       