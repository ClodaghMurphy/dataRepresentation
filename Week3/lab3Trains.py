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
#At the top of the program make an array called retrieveTags 
# that will store all the names of the tags we want to retrieve.
retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]
#Modify the program to print out each of the trains. 
#i.e. find the listings and iterate through them to print each out. Check it works.
#listings=soup.findAll("objTrainPositions")
   
#for listing in listings:
#    print(listing)
#modify the program so that it prints out the latitudes
#    print(listing.TrainLatitude.string)
#Store this property into a CSV:
#Before the for loop open the CSV file, 
#I am using with, so make sure that you indent the for loop so that it is in the with block.

with  open('week03_train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL) 


    listings = soup.findAll("objTrainPositions")
#We are only going to store trains that are south of Dublin (approx. 53.4)
#In the for loop of the listings before we make the entry list get the latitude 
# of this train and store it as a float, then check if it is less then the latitude of Dublin 
# (approx. 53.4)    
    for listing in listings:
        print(listing)
        lat =float( listing.TrainLatitude.string) 
        if (lat < 53.4): 


            entryList = [] #in the for loop now create an array called entryList
            for retrieveTag in retrieveTags:
                entryList.append(listing.find(retrieveTag).string)#append is a for loop that iterates through the tagnames
            train_writer.writerow(entryList) #append in the latitude and store that in the CSV.
