from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from dharam_api.serializer import  GroupSerializer,User_detailsSerializer,feedbackSerializer,InvoiceSerializer,HistorySerializer
from dharam_api.models import User_details 
from dharam_api.models import Invoice as invo
from decimal import Decimal
from dharam_api.models import History

from dharam_api.models import feedback as user_feedback
import datetime
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


class InvoiceViewSet(viewsets.ModelViewSet): 
    queryset = invo.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated] 


class HistoryViewSet(viewsets.ModelViewSet): 
    queryset = History.objects.all()
    serializer_class = HistorySerializer
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


class feedbackViewSet(viewsets.ModelViewSet): 
    queryset = user_feedback.objects.all()
    serializer_class = feedbackSerializer
    permission_classes = [permissions.IsAuthenticated] 



class feedback(GenericAPIView):
   def post(self, request, *args, **kwargs):
        userfeedback = json.loads(self.request.body.decode())['userfeedback']
        email = json.loads(self.request.body.decode())['email']
        print(userfeedback)
        check_email = User_details.objects.get(email=email)
        if userfeedback and check_email:
            if json.loads(self.request.body.decode())['userfeedback'] :
                 user_id= check_email.id
                 save = user_feedback(user_id__id=user_id,userfeedback=userfeedback,date=datetime.datetime.now())
                 save.save()
                 if save:
                    response = {
                        'massege': "userfeedback update successfully",
                        }
                    print(json.dumps(response, indent=4))
                    return HttpResponse((json.dumps(response, indent=4)))
            else:
                    return HttpResponse("feedback not found")
        else:
                return HttpResponse("user Not found")



class Invoice(GenericAPIView):
   def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        data = data.get('date')
        status = data.get('status')
        print(data)
        check_email = User_details.objects.filter(email=customer_email).first()
        if data and check_email:
            customer_name = check_email.name
            customer_email = check_email.email
            # mobile_number = invo.objects.count() + 1
            date = datetime.datetime.now().date()
            total_amount = Decimal(data.get('total_amount', 0))
            invoice = invo(mobile_number=status, date=date,customer_name=customer_name, customer_email=customer_email, total_amount=total_amount)
            invoice.save()
            if invoice:
                response = {'message': "Invoice updated successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("Invalid request parameters or user not found", status=400)



class History(GenericAPIView):
   def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        number = data.get('mobile_number')
        customer_email = data.get('customer_email')
        print(number)
        check_email = User_details.objects.filter(email=customer_email).first()
        if number and check_email:
            # Get values from data or initialize them
            customer_name = data.get('customer_name', '')
            total_amount = data.get('total_amount', 0)
            
            # Remove unnecessary line
            # data = data.name
            
            # Remove unnecessary line
            # status = status.status
            
            date = datetime.datetime.now().date()
            time = Decimal(data.get('time', 0))
            invoice = invo(mobile_number=number, date=date, customer_name=customer_name, customer_email=customer_email, total_amount=total_amount)
            invoice.save()
            if invoice:
                response = {'message': "Invoice updated successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("Invalid request parameters or user not found", status=400)



