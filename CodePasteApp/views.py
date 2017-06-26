# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from models import Code
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
        c = Code(data=request.POST['codedata'])
        c.title = request.POST['title']
        unique_string = get_random_string(5)
        success = False
        while success==False:
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
    obj.delete()
    return HttpResponseRedirect("/")