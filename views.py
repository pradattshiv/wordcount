from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1> first page </h1> ")