from django.shortcuts import render, redirect
from .models import *
from . import text_field_check
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def portal(request):
    return render(request, 'portal.html')


def compliment(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        compliment = request.POST.get('compliment')

        details = compliment_model(name=name, email=email, phone_number=phone_number, compliment=compliment)
        details.save()

        return render(request, 'Success.html')


    return render(request, 'compliment.html')


def suggestion(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        suggestion = request.POST.get('suggestion')

        details = suggestion_model(name=name, email=email, phone_number=phone_number, suggestion=suggestion)
        details.save()

        return render(request, 'Success.html')

    return render(request, 'suggestion.html')


def incident(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        incident_with = request.POST.get('incident_selected')
        incident = request.POST.get('incident')

        details = incident_model(name=name, phone_number=phone_number, location=location, incident_with=incident_with, incident=incident)
        details.save()

        return render(request, 'Success.html')

    return render(request, 'incident.html')


def feedback(request):

    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('selected_city')
        police_station = request.POST.get('station')

        answer1 = request.POST.get('answer_1')
        answer2 = request.POST.get('answer_2')
        answer3 = request.POST.get('answer3')
        answer4 = request.POST.get('answer_4')
        answer5 = request.POST.get('answer_5')
        answer6 = request.POST.get('answer6')
        answer7 = request.POST.get('answer7')
        answer8 = request.POST.get('answer8')
        answer9 = request.POST.get('answer9')
        answer10 = request.POST.get('answer10')

        overall_rating = request.POST.get('rating')
        written_feedback = request.POST.get('written_feedback')

        positive_or_negative = text_field_check.neg(written_feedback)

        details = feedback_model(name=name,email=email, phone_number=phone_number, city=city, police_station=police_station,
                                 answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5,
                                 answer6=answer6, answer7=answer7, answer8=answer8, answer9=answer9, answer10=answer10,
                                 overall_rating=overall_rating, written_feedback=written_feedback, positive_or_negative=positive_or_negative)
        
        details.save()

        return render(request, 'Success.html')


    return render(request, 'feedback_form.html')


def home(request):

    return render(request, 'home.html')



def signin(request):

    if request.method =="POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'Success_for_SignIn.html', {'fname': fname})

        else:
            messages.error(request, 'Bad Credentials!')
            return redirect('login')

    return render(request, 'login.html')



def signup(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('selected_city')
        police_station = request.POST.get('police_station_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # User Authentication

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = police_station
        myuser.is_active = True

        myuser.save()

        # Saving in Django model

        details = signup_model(email=email, phone_number=phone_number, city=city, police_station=police_station, username=username, password=password)
        details.save()

        return render(request, 'login.html')

    return render(request, 'SignUp.html')

