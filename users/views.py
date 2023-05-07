from venv import create
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegisterSerializer

def user(request):
    return render(request, 'users.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        conf_password=request.POST['conf_password']
        email=request.POST['email']

        #validation
        error_message=None

        value={
            'username':username,
            'email':email,
            'first_name':first_name,
            'last_name':last_name
        }

        if password != conf_password:
            error_message='Password not matching'
        elif User.objects.filter(username=username).exists():
            error_message='Username is already taken'
        elif User.objects.filter(email=email).exists():
            error_message='Email address is already registered'
        
        if not error_message:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
            return redirect('login')
        else:
            data={
                'error':error_message,
                'value':value
            }
            return render(request,'register.html',data)
    else:
        return render(request,'register.html')


class UserLogin(APIView):
    def post(self,request):
        username=request.data["username"]
        password=request.data["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return Response({"Message":"Login Sucsessfull"})
        else:
            return Response({"Message":"Invalid Credentials"})
        

class UserRegister(APIView):
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user=serializer.save()
            
            data['response']='user registered'
            data['username']=user.username
            data['email']=user.email
            data['first_name']=user.first_name
            data['last_name']=user.last_name
            token,create=Token.objects.get_or_create(user=user)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)

class welcome(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)