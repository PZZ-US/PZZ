from django.shortcuts import render
from django.http import HttpResponse

def simplehttp(response):
    return HttpResponse("<h1>HI user </h1>")