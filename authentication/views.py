from rest_framework import serializers, generics
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .serializers import *

class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer































    
# from django.http import HttpResponse
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from movies import settings
# from movies.settings import conn
# from django.contrib.sites.shortcuts import get_current_site



# Create your views here.
# def home(request):
#     pass

# def signup(request):
#     if request.method == "POST":

#         username = request.POST['username']
#         email = request.POST['email']
#         secretw = request.POST['secretw']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         if User.objects.filter(username=username):
#             messages.error(request, "Username already exists.")
#             return redirect('home')

#         if User.objects.filter(email=email):
#             messages.error(request, "Email already registered.")
#             return redirect('home')

#         if pass1 != pass2:
#             messages.error(request, "Passwords do not match!")

#         if not username.isalnum():
#             messages.error(request, "Invalid username!")
#             return redirect('home')


#         myuser = User.objects.create_user(username, email, secretw, pass1)
#         myuser.first_name = username
#         myuser.save()

#         messages.success(request, "Your account has been successfully created.")

#     return render(request, 'authentication/signup.html')

# def signin(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['pass1']

#         user = authenticate(username=username, password=pass1)

#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             return render(request, 'authentication/index.html', {'fname': fname})

#         else:
#             messages.error(request, 'Bad Credentials!')
#             return redirect('home')

#     return render(request, 'authentication/signin.html')

# def signout(request):
#     logout(request)
#     messages.success(request, "Logged out successfully.")
#     return redirect('home')

    