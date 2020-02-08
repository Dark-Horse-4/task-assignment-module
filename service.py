import os
import sys
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_app.settings")
#form django.contrib.auth.models import User
from todo_view.models import Task


objects = Task.objects.all()
print(objects)