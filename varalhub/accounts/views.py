import requests
import json
from django.db.models import  Q
from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

User = get_user_model()


# Create your views here.

class RegisterUser(View):
  template_name = "register.html"

  def get(self,request,*args,**kwargs):
    return render(request, self.template_name, {})

  def post(self, request, *args, **kwargs):
    if request.is_ajax() and request.method == "POST":
      data = request.POST
      # save to DB
      savedUser = User.objects.create_user(email=data["email"],
                                           username=data["username"],
                                           password=data["password1"],
                                           country=data["country"]
                                           )
      # return ajax response
      if savedUser is not None:
        return HttpResponse(json.dumps({"success":"You were Successfully registered ","registered":True}),content_type="application/json", status = 201)
      else:
        return HttpResponse(json.dumps({"error":"Could not register your details, try again"}),content_type="application/json", status = 404)  

    return render(request, self.template_name, {})

class LoginUser(View):
  template_name = "login.html"

  def get(self,request,*args,**kwargs):
    return render(request, self.template_name, {})

  def post(self,request,*args,**kwargs):
    if request.is_ajax() and request.method == "POST":
      if request.user.is_authenticated:
          return HttpResponse(json.dumps({"error":"You are already authenticated","logged":True}),content_type="application/json", status = 404) 

      # else get user data and authenticate
      data = request.POST
      print(data)
      email = data['login_email']
      password = data['login_pass']

      # server side validation
      if(email is None or email == ""):
        return HttpResponse(json.dumps({"error":"Please ennter your registered email address."}),content_type="application/json", status = 404) 
      if(password is None or password == ""):
          return HttpResponse(json.dumps({"error":"Please ennter your registered password.."}),content_type="application/json", status = 404) 

      # 
      qs = User.objects.filter(
          Q(email__iexact=email)
          ).distinct()

      if qs.count() == 1:
          user_obj = qs.first()
          if user_obj.check_password(password):
              user = user_obj      
              return HttpResponse(json.dumps({"success":"You were Successfully registered ","logged":True}),content_type="application/json", status = 201)
      return HttpResponse(json.dumps({"error":"Invalid credentials, please enter your registered email and password"}),content_type="application/json", status = 404) 
      
    return render(request, self.template_name, {})

def logoutUser(request):
  if request.user.is_authenticated:
    logout(request)
  return render(request,"login.html", {})
  

