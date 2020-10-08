#an exercise to read the html in from a file
from bs4 import BeautifulSoup
#it just opens the file and sends contents to BeautifulSoup
#there it is parsed and stored in memory as a DOM tree
with open("../Week2/carviewer2.html") as fp:
#fp means file pointer
    soup = BeautifulSoup(fp,'html.parser')#html.parser built into BeautSoup

print (soup.prettify())#prettify puts each tag onto a new line