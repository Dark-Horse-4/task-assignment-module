from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import Task
from django.contrib.auth.models import User
from datetime import date, timedelta, datetime
import pdb

@shared_task
def mailer(subject, message, recipient_list,a):
    pdb.set_trace()
    user = int(a)
    d = Task.objects.get(assignee = user)
    duedate = str(d.due_date)
    print(duedate)
    email = 'sivaramelumalai4032588@gmail.com'
    list_mail = list(email)
    now  =str( date.today()+timedelta(days=1))
    print(now)
    if duedate == now :
        send_mail(subject, message, recipient_list, 'sivaramelumalai4032588@gmail.com')
    else:
        print('not executed')
        
    