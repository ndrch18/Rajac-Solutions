from django.shortcuts import render

def hello_world(request):
    return render(request, 'system_app/hello_world.html')