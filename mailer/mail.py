from django.core.mail import send_mail
import datetime


def mail():
    name  = "sivaram"
    date = "10 dec"
    Subject = "test mail"
    Content = 'You have been assigned with the new task by '+name+'.The Due date to complete this is' + date
    print('hello')
    # send_mail(Subject, Content, 'sivaramelumalai4032588@gmail.com', ['sivaramelumalai4032588@gmail.com'], fail_silently=False)
