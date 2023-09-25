from django.http import HttpResponse

def index(request):
    # body
    return HttpResponse('<h1>Welcome to Django</h1>')

def home(request):
    return HttpResponse('<h3>Welcome to My Blog...</h3>')

