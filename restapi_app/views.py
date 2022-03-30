from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib import messages

from restapi_app.serializers import Userserialiser
import requests

from restapi_app.templates.base_urls import user_url

User = get_user_model()
# Create your views here.
from rest_framework.decorators import api_view


@api_view(['POST'])
def LoginView(request):
    if request.method=='POST':
        email =request.data.get('email')
        password = request.data.get('password')
        if authenticate(email=email,password=password):
            user=User.objects.get(email=email)
            return Response({'status':True,'User':{'id':user.id,'username':user.username,'phone':user.phone}})
        else:
            return Response({'status':False,'User':{'username':''}})

@api_view(['POST'])
def User_Registrations(request):
    if request.method=='POST':
        username=request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response("This user already exist")
        else:
            User.objects.create_user(username=username,password=password,email=email)
            user =User.objects.all()
            serializer =Userserialiser(user,many=True)
            return Response(serializer.data)

@api_view(['POST'])
def profileDetails(request,user_id):
    if request.method=='POST':
        id =user_id
        dob=request.data.get('DOB')
        city = request.data.get('city')
        country = request.data.get('country')
        phone =request.data.get('phone')

        if User.objects.get(id=id):
           user=User.objects.filter(id=id).values()
           updatevalues={}
           updatevalues['phone']=phone
           updatevalues['city']=city
           updatevalues['country']=country
           updatevalues['DOB']=dob
           user.update(**updatevalues )
           serializer =Userserialiser(user,many=True)
           return Response(serializer.data)
        else:
            return Response('not valid user')

def Viewhome(request):
    return render(request,'home_page.html')

def homelogin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        print(email)
        password=request.POST.get('password')
        print(password)
        response = requests.post(user_url+'login',data={'email':email,'password':password}).json()
        a=response['status']
        user=response['User']
        try:
            user_id=user['id']
            if user_id!="null":
              if a==True:
                 return render(request,'profile_page.html',{'user_id':user_id})
              else:
                 messages.success(request, "This user not valid")
                 return redirect('login_page.html')
            else:
                messages.success(request, "This user not valid")
                return render(request,'login_page.html')
        except:
            messages.success(request, "This user not valid")
            return render(request,'login_page.html')

    return render(request,'login_page.html')

def RegistrationPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email = request.POST.get('email')
        response = requests.post(user_url+'User_Registrations',data={'username':username,'password':password,'email':email}).json()
        if response=='This user already exist':
          messages.success(request, "This user already exist")
          return render(request,'Registration.html')
        else:
          return render(request,'login_page.html')
    return render(request,'Registration.html')



def ProfilePage(request):
    if request.method=='POST':
        dob=request.POST.get('dob')
        print(dob)
        city=request.POST.get('city')
        print(city)
        country = request.POST.get('country')
        print(country)
        phone = request.POST.get('phone')
        print(phone)
        id=request.POST.get('user_id')
        print(id)
        response = requests.post(user_url+'addprofiledata/'+str(id) ,data={'DOB':dob,'city':city,'country':country,'phone':phone}).json()
        print(response)
        if response=='not valid user':
          messages.success(request, "not valid user")
          return render(request,'login_page.html')
        else:
          # user=response['User']
          messages.success(request, "profile added")
          return render(request,'profile_page.html')
    return render(request,'profile_page.html')

def view_profile(request):
    if 'id' in request.GET:
        id= request.GET.get('id')
        user = User.objects.get(id=id)
        return render(request,'view_profile.html',{'user':user})

