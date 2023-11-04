from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.mail import send_mail, EmailMessage
from Feedback import settings
from .forms import Feedback_Form


# Create your views here.

def form(request):
    if request.method == 'POST':
        
        name = None
        if request.POST['name'] is not None:
            name = request.POST['name']
        
        email = None
        if request.POST['email'] is not None:
            email = request.POST['email']
                  
        phone_number = None
        if request.POST['phone_number'] is not None:
            phone_number = request.POST['phone_number']
        
        city = request.POST['city']

        police_station = request.POST['police_station']

        ans1 = None
        if request.POST['answer1'] is not None:
            ans1 = request.POST['answer_1']
        
        ans2 = None
        if request.POST['answer2'] is not None:
            ans2 = request.POST['answer_2']

        ans3 = None
        if request.POST['answer3'] is not None:
            ans3 = request.POST['answer_3']
        
        ans4 = None
        if request.POST['1star'] is not None:
            ans4 = request.POST['1star']

        ans5 = request.POST['star-1']

        written_feedback = None
        if request.POST['written_feedback'] is not None:
            written_feedback = request.PST['written_feedback']




        # Define ID


        # Email Notification
        subject = 'New Feedback Submitted'
        message = f'''
Recieved an Feedback for your Police Station!
Please review it.

Thank You!
Your Feedback System
'''
        from_email = settings.EMAIL_HOST_USER
        to_list = ['krish.pundhir007@gmail.com']
        send_mail(subject, message, from_email, to_list, fail_silently= True)

        return redirect('home')
    
    else:
         form = Feedback_Form(None)
         return render(request, 'feedback_form.html', {'form':form})


def submit(request):

    if request.method == 'POST':
        
        name = None
        if request.POST['name'] is not None:
            name = request.POST['name']
        
        email = None
        if request.POST['email'] is not None:
            email = request.POST['email']
                  
        phone_number = None
        if request.POST['phone_number'] is not None:
            phone_number = request.POST['phone_number']
        
        city = request.POST['city']

        police_station = request.POST['police_station']

        ans1 = None
        if request.POST['answer1'] is not None:
            ans1 = request.POST['answer_1']
        
        ans2 = None
        if request.POST['answer2'] is not None:
            ans2 = request.POST['answer_2']

        ans3 = None
        if request.POST['answer3'] is not None:
            ans3 = request.POST['answer_3']
        
        ans4 = None
        if request.POST['1star'] is not None:
            ans4 = request.POST['1star']

        ans5 = request.POST['star-1']

        written_feedback = None
        if request.POST['written_feedback'] is not None:
            written_feedback = request.PST['written_feedback']




        # Define ID


        # Email Notification
        subject = 'New Feedback Submitted'
        message = f'''
Recieved an Feedback for your Police Station!
Please review it.

Thank You!
Your Feedback System
'''
        from_email = settings.EMAIL_HOST_USER
        to_list = ['krish.pundhir007@gmail.com']
        send_mail(subject, message, from_email, to_list, fail_silently= True)

        return redirect('home')
    
    else:
         form = Feedback_Form(None)
         return render(request, 'feedback_form.html', {'form':form})

def portal(request):
    return render(request, 'portal.html')
"""
def feedback(request):
    if request.method == 'POST':
        details = Feedback_Form(request.POST)

        if details.is_valid():

            feedback_form = details.save(commit=False)

            feedback_form.save()

            return redirect('portal.html')
        
        else:
            return render(request, 'feedback_form.html', {'form':details})
        
    else: 
        form = Feedback_Form(None)
        return render(request, 'feedback_form.html', {'form':form})
"""

def trial(request):

    if request.method=='POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        details = trial_model(name=name, email=email, phone_number=phone_number)

        details.save()

        return render(request, 'portal.html')

    return render(request, 'feedback_form.html')

def trial2(request):

    if request.method=='POST':

        city = request.POST.get('city')
        police_station = request.POST.get('police_station')

        details = trial_model2(city=city, police_station=police_station)

        details.save()

        return render(request, 'portal.html')

    return render(request, 'feedback_form.html')


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

        details = feedback_model(name=name,email=email, phone_number=phone_number, city=city, police_station=police_station,
                                 answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5,
                                 answer6=answer6, answer7=answer7, answer8=answer8, answer9=answer9, answer10=answer10,
                                 overall_rating=overall_rating, written_feedback=written_feedback)
        
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
