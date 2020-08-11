from django.db import models
from django.utils import timezone

#create you models here
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
        
class challan(models.Model):
    license_no = models.CharField(max_length=15)
    comment = models.CharField(max_length = 100, null = True)
    amount = models.FloatField( default =0)
    date = models.DateTimeField(default = timezone.now)
    
class user(models.Model):
    u_name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10, default = '000')
    active = models.BooleanField(default = True)
    f_name= models.CharField(max_length=10, null = True)
    l_name = models.CharField(max_length=10, null = True)
    licence_no = models.CharField(max_length=15, unique=True, primary_key = True)
    e_mail = models.EmailField(null = True)

class p_user(models.Model):
    pu_name = models.CharField(max_length = 10,null = True)
    password = models.CharField(max_length = 10, null= True)
    e_mail = models.EmailField( null = True)

class diversion(models.Model):
    start = models.CharField( max_length = 20 , null=True)
    dest = models.CharField(max_length = 20, null = True)
    date = models.DateTimeField(default = timezone.now)
    diver = models.CharField(max_length=10, null =True)
    
class news(models.Model):
    heading = models.CharField(max_length = 50,null = True)
    content = models.CharField(max_length = 200,null = True)
    date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.heading
    
class  media(models.Model):
    img = models.ImageField(upload_to='pics')
    date = models.DateTimeField(default = timezone.now)
    heading = models.CharField(max_length = 100)

class enquiry(models.Model):
    e_mail = models.CharField(max_length=25)
    u_name = models.CharField(max_length = 35)
    subject = models.CharField(max_length =40, null = True) 
    issue = models.CharField(max_length = 100)
    
    
