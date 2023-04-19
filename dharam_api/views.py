from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from dharam_api.serializer import  GroupSerializer,User_detailsSerializer,feedbackSerializer,InvoiceSerializer,HistorySerializer,NoticationsSerializer,User_SettingsSerializer
from dharam_api.models import User_details 
from dharam_api.models import Invoice as invo
from decimal import Decimal
from dharam_api.models import History,Notications, User_Settings
from dharam_api.models import feedback as user_feedback
import datetime
from rest_framework import generics, permissions
from rest_framework.response import Response
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

class noticationsViewSet(viewsets.ModelViewSet): 
    queryset = Notications.objects.all()
    serializer_class = NoticationsSerializer
    permission_classes = [permissions.IsAuthenticated] 

class User_SettingsViewSet(viewsets.ModelViewSet): 
    queryset = User_Settings.objects.all()
    serializer_class = User_SettingsSerializer
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
                        'massege': "userfeedback  successfully",
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
        number = data.get('mobile_number')
        check_email = data.get('check_email')
        print(number)
        check_email = User_details.objects.filter(email=customer_email).first()
        if number and check_email:
            customer_name = check_email.name
            customer_email = check_email.email
            number = Invoice.objects.count() + 1
            date = datetime.timezone.now().date()
            total_amount = Decimal(data.get('total_amount', 0))
            invoice = Invoice(number=number, date=date, customer_name=customer_name, customer_email=customer_email, total_amount=total_amount)
            invoice.save()
            if invoice:
                response = {'message': "Invoice updated successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("Invalid request parameters or user not found", status)
class history(GenericAPIView):
   def post(self, request, *args, **kwargs):
        date = request.data.get('date')
        location=request.data.get('location')
        status = request.data.get('status')
        time=request.data.get('time')
        accepted=request.data.get('accepted')
   
        if status :
            date = datetime.datetime.now().date()
            time = datetime.datetime.now().time()
            accepted = Decimal(request.data.get('accepted', 0))
            history = History(date=date, location=location,status=status, time=time, accepted=accepted)
            history.save()
            if history:
                response = {'message': "History  successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("History request parameters or user not found", status=400)
 
class notications(GenericAPIView):
   def post(self, request, *args, **kwargs):
        accepted = request.data.get('accepted')
        posted=request.data.get('posted')
        date = request.data.get('date')
           
        if posted :
            date = datetime.datetime.now().date()
            accepted = request.data.get('accepted')
            notications = Notications(accepted=accepted, posted=posted,date=date)
            notications.save()
            if notications:
                response = {'message': "Notications  successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("Notications request parameters or user not found", status=400)

class whatsapp(GenericAPIView):
   def post(self, request, *args, **kwargs):
        whatsapp_number = request.data.get('whatsapp_number')
        Notications_on=request.data.get('Notications_on')
        print(whatsapp_number)
        print(Notications_on)
        if Notications_on :
            Notications_on = request.data.get('Notications_on')
            Settings = User_Settings(whatsapp_number=whatsapp_number,Notications_on=Notications_on)
            Settings.save()
            if Settings:
                response = {'message': "whatsapp  successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("whatsapp request parameters or user not found", status=400)

class Emergency_number(GenericAPIView):
   def post(self, request, *args, **kwargs):
        emergency_number = request.data.get('emergency_number')
        Notications_on=request.data.get('Notications_on')
        
        if Notications_on :
            # date = datetime.datetime.now().date()
            Notications_on = request.data.get('Notications_on')
            Settings = User_Settings(emergency_number=emergency_number,Notications_on=Notications_on)
            Settings.save()
            if Settings:
                response = {'message': "Emergency_number  successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("Emergency_number request parameters or user not found", status=400)  


class select_Hospital(GenericAPIView):
   def post(self, request, *args, **kwargs):
        select_Hospital = request.data.get('select_Hospital')
        
        if select_Hospital :
            Settings = User_Settings(select_Hospital=select_Hospital)
            Settings.save()
            if Settings:
                response = {'message': "Hospital_Name  successfully"}
                print(json.dumps(response, indent=4))
                return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
            
        return HttpResponse("Hospital_Name request parameters or user not found", status=400)         