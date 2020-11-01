import requests


#before running this code, make sure the restful api is running
#cd C:\ALL MY STUFF\GMIT\dataRepresentation\dataRepresentation\Week5\server
#python restserver.py
url = 'http://127.0.0.1:5000/cars'#DON'T USE LOCAL HOST!
#send something on up to cars
#make it a dict object, automatically converted to json
data = {'reg':'123','make':'blah','model':'blah','price':1234}
#
response = requests.post(url, json=data)
#that is post but you could also do, put, get, delete
print(response.status_code)
print(response.json())#empty argument- very important
