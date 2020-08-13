from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.conf import settings
import requests
import json
 

def home(request):
  return render(request,"index.html",{})

def createAccount(request):
  return render(request,"account.html",{})

def wishlist(request):
  return render(request,"wishlist.html",{})

def mycart(request):
  return render(request,"cart.html",{})

def checkout(request):
  return render(request,"checkout.html",{})

def contactus(request):
  return render(request,"contactus.html",{})