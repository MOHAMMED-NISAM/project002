# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Welcome')


def sampleFun(request):
    return render(request, 'form.html')


def indexFun(request):
    return render(request, 'index.html')

def homeFun(request):
    return render(request, 'home.html')


def testFun1(request):
    return render(request, 'home.html')