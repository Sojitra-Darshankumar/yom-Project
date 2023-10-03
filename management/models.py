from django.db import models
from django.forms import ModelForm

# Create your models here.

# --------------------------------------------------------------- Admin Models ------------
class admin1(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Retypepassword = models.CharField(max_length=100)
    Picture = models.FileField(max_length=100,upload_to='',default='')
    Contact = models.BigIntegerField(default='0')

class admin1form(ModelForm):
    class Meta:
        model = admin1
        fields = ["Name","Email","Password","Retypepassword","Picture","Contact"]

# -------------------------------------------------------------- Slider Models ------------

class slider(models.Model):
    Tital = models.CharField(max_length=100)
    Description = models.TextField()
    Picture = models.FileField(max_length=100,upload_to='',default='')

class sliderform(ModelForm):
    class Meta:
        model = slider
        fields = ["Tital","Description","Picture"]

# ------------------------------------------------------------ Services Models ------------

class services(models.Model):
    Icon = models.CharField(max_length=100)
    Tital = models.CharField(max_length=100)
    Description = models.TextField()

class servicesform(ModelForm):
    class Meta:
        model = services
        fields = ["Icon","Tital","Description"]

# ------------------------------------------------------- Blog Category Models ------------

class blogcategory(models.Model):
    Name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Name

class blogcategoryform(ModelForm):
    class Meta:
        model = blogcategory
        fields = ["Name"]

# ---------------------------------------------------------------- Blog Models ------------

class blog(models.Model):
    Tital = models.CharField(max_length=100)
    Description = models.TextField()
    Picture = models.FileField(max_length=100,upload_to='',default='')
    Cat_id = models.ForeignKey(blogcategory,on_delete=models.CASCADE,default='')
    Admin_id = models.BigIntegerField()

class blogform(ModelForm):
    class Meta:
        model = blog
        fields = ["Tital","Description","Picture","Cat_id","Admin_id"]




# python manage.py migrate
# python manage.py makemigrations