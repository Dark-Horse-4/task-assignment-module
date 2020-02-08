from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.core.mail import send_mail


class Task(models.Model):
    priority_choices = [('1','high'),('2','medium'),('3','low')] 
    assignee = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField( choices = priority_choices , max_length=50)
    is_completed = models.BooleanField(default= False)
    
    
    def __str__(self):
        return self.priority
    
    def get_absolute_url(self):
        return reverse("home")
    

def save(sender, instance,*args,**kwargs):
        send_mail('verification', 'Sign up message.', 'sivaramelumalai4032588@gmail.com', ['sivaramelumalai4032588@gmail.com',], fail_silently=False)


post_save.connect(save,sender=Task)
        
        
class UserImage(models.Model):
    image = models.ImageField(upload_to='profile_pics',default = 'profile_pics/index.png' ,height_field=None, width_field=None, max_length=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
        

