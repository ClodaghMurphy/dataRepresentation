import requests
import json
from xlwt import *

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)#use above url variable in a get request
data = response.json()

#output to console
print (data)

#output cars individualy 
for car in data["cars"]:
    print (car)

#other code
#save this output to a file
filename = 'cars.json'
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# write to excel file
#the workbook part
w = Workbook()
ws = w.add_sheet('cars')#add a sheet to your workbook
row = 0;
ws.write(row,0,"reg")#identify where you want the data to go (on rows)
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1 
for car in data["cars"]:#extracting specific data onto specific row locations
    ws.write(row,0, car["reg"])
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row += 1

w.save('cars.xls')
#do ls and then open up cars.xls to view it on your own computer