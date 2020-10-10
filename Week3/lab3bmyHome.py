#Example of extracting data from a website that is not designed to do so
#you have to figure out the url of the page class, ids etc,.
#if myhome.ie change the design of the site, this program should be updated.
import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/tipperary/property-for-sale?page=7")

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#the delimiter is up to you to choose!

listings = soup.findAll("div", class_="PropertyListingCard" )
#search on source/elements page to identify the div classes you are interested in
#CTRL F on the source page 
for listing in listings:
    entryList = []#make a list with the categories you wish to see

    price = listing.find(class_="PropertyListingCard__Price").text 
    entryList.append(price) 
    address = listing.find(class_="PropertyListingCard__Address").text 
    entryList.append(address) 
    
    home_writer.writerow(entryList)
home_file.close()#close the files when you are finished writing the rows