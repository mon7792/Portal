from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from datetime import datetime


# Create your models here.

class User(AbstractUser):
    #Personal Info
    Bio = models.CharField(max_length=100, default="Enter the Bio")
    CapGID = models.PositiveIntegerField(default= 666666 ,validators=[MaxValueValidator(999999)])
    DOB = models.DateField(default=datetime.now)
    
    #SJM Details
    SJMID = models.PositiveIntegerField(default= 666666 ,validators=[MaxValueValidator(999999)])
    SJMBillableDate = models.DateField(default=datetime.now)
    SJMEMAILID = models.EmailField(default="xxx@sjm.com",  max_length = 18)
    
    #ODC Details:
    DeskNo = models.CharField(default="MUM-ARL-W0003",max_length = 25)
    #ASSEST
    
    #ROLE
    ROLE_CHOICES = (
    ('FR', 'Fresher'),
    ('SR', 'Senior'),
    ('TL', 'Team Lead'),
    ('PL', 'Project Lead'),
    ('TS', 'Technical Specialist'),
    ('M', 'Manager'),
    ('SM', 'Senior Manager'),
    ('DM', 'Delivery Manager'),
    ('AD', 'Associate Director'),
    )
    ROLE = models.CharField( max_length = 2, choices = ROLE_CHOICES, default="Fresher")
    MANAGER = models.CharField(default="Manager Name", max_length = 18)
    
    def __str__(self):
        return self.username
