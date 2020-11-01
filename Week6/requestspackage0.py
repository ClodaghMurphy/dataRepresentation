#Making a request with Requests is very simple.
#Begin by importing the Requests module:

import requests
#Create a variable called URL
url = 'https://www.gmit.ie'
response = requests.get(url)#you could also do it like this r = requests.get('https://www.gmit.ie')
#Now, we have a Response object called resonse. We can get all the information we need from this object.
#Requests’ simple API means that all forms of HTTP request are as obvious.

print (response.status_code)#I got 200
print (response.headers)#A list of headers in json format


