# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from CodePasteApp.models import Code
from django.template import loader
from django.utils.crypto import get_random_string
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def HomeView(request):
    template = loader.get_template("CodePasteApp/home.html")
    context = {"codes":"codes"}
    return HttpResponse(template.render(context,request))

def GetCode(request,string):
    codes = get_object_or_404(Code,link=string)
    context = {"codes":codes}
    template = loader.get_template("CodePasteApp/get_code.html")
    return HttpResponse(template.render(context,request))

def Create(request):
    if request.method == 'POST':
        checkdata = request.POST['codedata']
        if(checkdata == ''):
            return HttpResponseRedirect("/")
        c = Code(data=request.POST['codedata'])
        c.title = request.POST['title']
        c.password = request.POST['password']
        success = False
        while success==False:
            unique_string = get_random_string(5)
            try:
                obj = Code.objects.get(link=unique_string)
                success = False
            except ObjectDoesNotExist:
                success = True
        c.link = unique_string
        c.save()
        return HttpResponseRedirect("/"+unique_string+"/")

def Delete(request,string):
    obj = get_object_or_404(Code,link=string)
    if obj.password == request.POST['password']:
        obj.delete()
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/"+obj.link+"/")


def Update(request,string):
    obj = get_object_or_404(Code, link=string)
    if(obj.password == request.POST['password']):
            Code.objects.filter(link=string).update(data=request.POST['codedata'])
    return HttpResponseRedirect("/" + obj.link + "/")
