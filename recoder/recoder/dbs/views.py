from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, workd. you're at the dbs index")

