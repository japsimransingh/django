from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1> this is 'home page'</h1>")
