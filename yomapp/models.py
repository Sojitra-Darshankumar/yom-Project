from django.db import models
from django.forms import ModelForm
from management.models import blog


# Create your models here.

# ------------------------------------------------------------ Comments Models ------------

class comments(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Picture = models.FileField(max_length=100,upload_to='',default='')
    Subject = models.CharField(max_length=100)
    Comment = models.TextField()
    Blogid = models.ForeignKey(blog,on_delete=models.CASCADE,default='')

class commentsform(ModelForm):
    class Meta:
        model = comments
        fields = ["Name","Email","Picture","Subject","Comment","Blogid"]

# ------------------------------------------------------------ Contact Models ------------

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

class Contactform(ModelForm):
    class Meta:
        model = Contact
        fields = ["Name","Email","Subject","Message"]

# ------------------------------------------------------- Work Category Models ------------

class Workcategory(models.Model):
    Name = models.CharField(max_length=100)
    

class Workcategoryform(ModelForm):
    class Meta:
        model = Workcategory
        fields = ["Name"]

# ---------------------------------------------------------------- Work Models ------------

class Work(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Picture = models.FileField(max_length=100,upload_to='',default='')
    Work_Category =  models.ForeignKey(Workcategory,on_delete=models.CASCADE,default='')
    

class Workform(ModelForm):
    class Meta:
        model = Work
        fields = ["Name","Description","Picture","Work_Category"]

# ------------------------------------------------------------- Clients Models ------------

class Clients(models.Model):
    Name = models.CharField(max_length=100)
    Link = models.CharField(max_length=1000,default='')
    Picture = models.FileField(max_length=100,upload_to='',default='')
    

class Clientsform(ModelForm):
    class Meta:
        model = Clients
        fields = ["Name","Link","Picture"]

# python manage.py migrate
# python manage.py makemigrations