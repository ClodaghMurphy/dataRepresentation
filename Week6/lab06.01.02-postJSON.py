# In this lab we are going to use Python to access the server we used in week05 via the API.
#To do this you must make sure that your server is running
# 2. Write a python program that creates a NEW car on the server by using the API


import requests
import json

dataString = {'reg':'08 T 1234','make':'Ford','model':'Prius','price':12324}
url = 'http://127.0.0.1:5000/cars'

response = requests.post(url, json=dataString)

print (response.status_code)