from django.db import models
from django.contrib.auth.models import AbstractUser, User
from .manage import UserManager

class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=10,default="")
    otp=models.BooleanField(default=False)
    username = ""

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects = UserManager()

class Challenges(User):
    problemstatement = models.TextField()
    sample_input_1 = models.TextField()
    sample_input_2 = models.TextField()
    sample_output_1 = models.TextField()
    sample_output_2 = models.TextField()
    explanations = models.TextField()
    #techstack = models.CharField(max_length=225)
    #language = models.CharField(max_length=225)
    class Stack(models.TextChoices):
        front = "1", "Frontend"
        back = "2", "Backtend"
        fstack = "3", "FullStack"
        machine = "4", "AI/ML"
        danylasis = "5", "Data Analyst"
        dscience = "6", "Data Science"
        
    class Language(models.TextChoices):
        pyt = "1", "Python" 
        java = "2", "Java"
        cpp = "3", "CPP"
        # AI/Ml = "4", ""
        # dataanalysis= "5", "dataanalysi"
        # datascinece = "6", "datascinece"
    
    language = models.CharField(max_length=10, choices=Language.choices, default=Language.pyt)
    stack = models.CharField(max_length=20, choices=Stack.choices)
          
        