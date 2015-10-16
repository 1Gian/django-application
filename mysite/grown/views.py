from django.shortcuts import render
from django.Http import Responce

# Create your views here.


def index(request):
	return HttpResponce ("Success")
