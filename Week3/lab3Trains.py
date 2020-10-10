#Write a program that stores the data for all trains in Ireland in a csv file
#Use the Irish rail API
#http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML


import requests
import csv
from bs4 import BeautifulSoup
#Create a python program that reads the XML from the URL and prints it out, using beautifulSoup. 
url="http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page=requests.get(url)
# Check it does retrieve the data.
soup = BeautifulSoup(page.content,'xml')
#print(soup.prettify())

#Modify the program to print out each of the trains. 
#i.e. find the listings and iterate through them to print each out. Check it works.
listings=soup.findAll("objTrainPositions")
   
for listing in listings:
#    print(listing)
#modify the program so that it prints out the latitudes
    print(listing.TrainLatitude.string)
#Store this property into a CSV:
#Before the for loop open the CSV file, 
I am using with, so make sure that you indent the for loop so that it is in the with block.