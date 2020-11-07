import requests
import json

#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
#all you want is Balancing%20and%20Imbalance%20Market%20Cost%20View
#and on a particular date
#the host website gave information on how to specify search parameters
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date"
response = requests.get(url)
data = response.json()

listOfReports = []
#print(data)#output to console
for item in data["items"]:
    #print(item["ResourceName"])#you interrogate the page to identify the info that you want and what it is called
    listOfReports.append(item["ResourceName"])

#item["ResourceName"]
for ReportName in listOfReports:
    #print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    print(url)
    response= requests.get(url)
    aReport= response.json()

#other code
#save this to a file
filename = 'allreports.json'
# Writing JSON data
f =  open(filename, 'w')
json.dump(data, f, indent=4)