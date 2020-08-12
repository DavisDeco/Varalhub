from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.conf import settings
import requests
import json
 

def home(request):

    # if request.is_ajax() and request.method == "GET":
    #     residentialData = {}
    #     officesData = {}
    #     # agentsData = {}

    #     try:
    #         residentials = requests.get(settings.RESIDENTIAL_FEATURED_API_URL,timeout=10)
    #         offices = requests.get(settings.OFFICE_FEATURED_API_URL,timeout=10)
    #         # agents = requests.get(settings.FEATURED_AGENT_API_URL,timeout=10)

    #         if residentials.status_code == 200:
    #             if json.loads(residentials.content)['results']:
    #                 residentialData = json.loads(residentials.content)['results']

    #         if offices.status_code == 200:
    #             if json.loads(offices.content)['results']: 
    #                 officesData = json.loads(offices.content)['results'] 
            
    #         # if agents.status_code == 200:
    #         #     if json.loads(agents.content)['results']: 
    #         #         agentsData= json.loads(agents.content)['results'] 
            
    #         return HttpResponse(json.dumps({"success":"Retrived all featured data","residentialData":residentialData,"officesData":officesData}),status=200,content_type="application/json")

    #     except requests.exceptions.RequestException as e:
    #         return HttpResponse(json.dumps({"error":"Featured data not retrieved"}),status=404,content_type="application/json") 

  return render(request,"index.html",{})
