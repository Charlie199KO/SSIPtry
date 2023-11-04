from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length= 30, null= True, blank= True)
    email = models.EmailField(max_length= 50, null= True, blank= True)
    phone_number = models.IntegerField(null= True, blank= True)
    city = models.CharField(max_length= 15)
    station = models.CharField(max_length= 30)

    # Remove null= True once completed the form
    # Were you treated respectfully and professionally by the officer(s)?
    ans1 = models.CharField(max_length=3, null= True)

    # Were you provided with clear and understandable information about the actions taken by the police?
    ans2 = models.CharField(max_length=3, null= True)

    # How would you rate the response time to your calls or requests for assistance?
    ans3 = models.SmallIntegerField(null= True)

    # Were your concerns address to your satisfaction?
    ans4 = models.CharField(max_length= 3, null= True)

    # Overall Rating to police station
    ans5 = models.SmallIntegerField()

    # What, if anything, could the police department do better in the future? (Optional)
    textbox = models.CharField(max_length=300, null= True)


class trial_model(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class trial_model2(models.Model):
    city = models.CharField(max_length=20)
    police_station = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}"


class compliment_model(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    compliment = models.TextField()

    def __str__(self):
        return f"{self.name}"
    

class suggestion_model(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    suggestion = models.TextField()

    def __str__(self):
        return f"{self.name}"
    

class incident_model(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50)
    location = models.TextField()
    incident_with = models.CharField(max_length=50, null=True)
    incident = models.TextField()

    def __str__(self):
        return f"{self.name}"
    

class signup_model(models.Model):
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50, null=True)
    police_station = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username}"
    

class feedback_model(models.Model):

    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50)
    police_station = models.CharField(max_length=50)
    answer1 = models.CharField(max_length=10, null=True)
    answer2 = models.CharField(max_length=10, null=True)
    answer3 = models.CharField(max_length=10, null=True)
    answer4 = models.CharField(max_length=10, null=True)
    answer5 = models.CharField(max_length=10, null=True)
    answer6 = models.CharField(max_length=10, null=True)
    answer7 = models.CharField(max_length=10, null=True)
    answer8 = models.CharField(max_length=10, null=True)
    answer9 = models.CharField(max_length=10, null=True)
    answer10 = models.CharField(max_length=10, null=True)
    overall_rating = models.CharField(max_length=10, null=True)
    written_feedback = models.TextField(null=True)
