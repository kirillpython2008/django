from django.shortcuts import render

from hello_world.models import UserModel


def say_hello_world(request):
    UserModel.objects.create(username='Oleg', password='123')
    return render(request ,"index.html")
