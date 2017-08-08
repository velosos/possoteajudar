# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import requests
import json




def index(request):

    return render(request, 'index.html')     




def resultado(request,texto):

    texto = request.POST.get('texto')
	# Set the request parameters
    url = 'https://devglobo.service-now.com/api/now/table/kb_knowledge?sysparm_query=short_descriptionLIKE' + texto

# Eg. User name="admin", Password="admin" for this code sample.
    user = 'getkbs'
    pwd = 'globo'

# Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

# Decode the JSON response into a dictionary and use the data
    data = response.json()
    #print data

    print(data)
    

    return render(request, 'resultado.html',{'obj':data['result']})     


def body(request,protocolo):


	# Set the request parameters
    url = 'https://devglobo.service-now.com/api/now/table/kb_knowledge?sysparm_query=number='+protocolo

# Eg. User name="admin", Password="admin" for this code sample.
    user = 'getkbs'
    pwd = 'globo'

# Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

# Decode the JSON response into a dictionary and use the data
    data = response.json()
    #print data

    print(data)

    return render(request, 'body.html',{'obj':data['result']})

