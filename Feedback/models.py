from django.db import models

# Create your models here.

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
    positive_or_negative = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.name}"
