#4. Write a python program that deletes a car from the server using the API.
import requests

url = 'http://127.0.0.1:5000/cars/08%20T%201234'#identify the car to delete
#I have two cars with that reg and this programme deletes the first one
response = requests.delete(url)
print (response.status_code)
print (response.text)