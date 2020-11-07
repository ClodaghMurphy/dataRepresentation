import requests
import json
from xlwt import *


url= "https://prodapi.metweb.ie/observations/mt-dillon/today"

print (url)
response = requests.get(url)
data = response.json()

####OPTION A JSON
filename = 'metEireann.json'
#Write json data
f = open(filename, "w")
json.dump(data, f, indent=4)

#####OPTION B-print to the screen
for row in data:
    print(row["date"])
    
#####OPTION C - export to an excel
# write to excel file
#the workbook part
w = Workbook()
ws = w.add_sheet('todayMet')
rowNumber = 0;
ws.write(rowNumber,0,"reportTime")
ws.write(rowNumber,1,"temperature")
ws.write(rowNumber,2,"windSpeed")
ws.write(rowNumber,3,"cardinalWindDirection")
rowNumber += 1 
for row in data:#extracting specific data onto specific row locations
    ws.write(rowNumber,0,row["reportTime"])
    ws.write(rowNumber,1,row["temperature"])
    ws.write(rowNumber,2,row["windSpeed"])
    ws.write(rowNumber,3,row["cardinalWindDirection"])
    rowNumber += 1

   
w.save('mtDillonToday.xls')
#do ls and then open up mtDillonToday.xls to view it on your own computer
#don't forget to close it if you already have it open!