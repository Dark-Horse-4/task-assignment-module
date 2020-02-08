from django.apps import AppConfig
from mailer import mailer

class TodoViewConfig(AppConfig):
    name = 'todo_view'
    def ready(self):
        
        mailer.start()