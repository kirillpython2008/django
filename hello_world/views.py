from django.shortcuts import render


def say_hello_world(request):
    return render(request ,"index.html")
