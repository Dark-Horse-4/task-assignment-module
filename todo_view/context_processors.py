from django.contrib.auth.models import User


def all_users(request):
    return{ 'users': User.objects.all() }