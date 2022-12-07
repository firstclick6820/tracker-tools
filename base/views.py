# Import Django Modules
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Import rest Framework moduls
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
# Import Request Module
import requests

# Import Json for serializing the data
import json




# Import Phone Number Module for tracking the phone number country and service provider
import phonenumbers
from phonenumbers import geocoder, carrier, timezone



# Import Country Info modul for collection country information
from countryinfo import CountryInfo


# import socket, Platform and urllib to collect user information
import socket
import platform
import urllib.request










# This simple function return the mobile number information to the user
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def phonenumber_details(request, phonenumber):
    
    phonenumber = '{}{}'.format('+', phonenumber)
    # Parse the target Number details
    target_number = phonenumbers.parse(phonenumber)
    # Check if the number is a real number
    is_possible_number = phonenumbers.is_possible_number(target_number)
    # check if the number is valid
    valid = phonenumbers.is_valid_number(target_number)
    # Get the Country Code
    country = geocoder.country_name_for_number(target_number, "en")
    # Get Service Provider Information
    service_provider = carrier.name_for_number(target_number, 'en')
    # Get the Time Zone.
    time_zone = timezone.time_zones_for_number(target_number)
    
    # Additional : Making Various Formats
    format_national = phonenumbers.format_number(target_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    format_international = phonenumbers.format_number(target_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    format_e164 =  phonenumbers.format_number(target_number, phonenumbers.PhoneNumberFormat.E164)
   
    # Formating the data to 
    
    context = {

        "Is_valid": valid,
        "is_possible_number":is_possible_number ,
        "Country": country,
        "Service Provider": service_provider,
        "Time Zone" : time_zone,
        
        "Addtional": {
            
            "Country_Code": target_number.country_code,
            "Formats": {
                
            "National_Format": format_national,
            "International_Format": format_international,
            "ES164_Format": format_e164
            
             }, 
            
        },
      
    }

    return HttpResponse(JsonResponse(context))















# This simple function returns the country information
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def countryInformation(request, country):   
    country_info = {
        "Country_details": CountryInfo(country).info(),
    }

    return JsonResponse(country_info, safe=False)
    
    
    



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def seracher_details(request):
    # Use Urllib to grap the external IP address of a user
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    
    # Use Socket to get the Internal IP address of a user
    hostname = socket.gethostname()
    IPAddress = socket.gethostbyname(hostname)
    
    
    # Use Platform to grap the user device information
    system_information = platform.uname()
 
    # Use the below url to find out  user Location provided the ISP (internet Service Provider).
    request_url = 'https://geolocation-db.com/jsonp/' + external_ip
    # Store the result in a variable
    response = requests.get(request_url)
    # Decode the respone
    result = response.content.decode()
    
    # Clean the returned string so it just contains the dictionary data for the IP address
    result = result.split("(")[1].strip(")")
    # Convert this data into a dictionary

    

    
    
    # Design the context module to send the data to user
    searcher_details = {
        
        "Location":json.loads(result),
        "External IP": external_ip,
        "Internal IP": IPAddress,
        "HostName": hostname,
        "system_infomration": system_information
        
    }
    
    return JsonResponse(searcher_details, safe=False)