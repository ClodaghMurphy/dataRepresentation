###Write a python program that will read in a html page from a file and prints it out again###


#Where a html doc made in a previous week is converted to a pdf
#that is not a big deal in itself e.g.I could chose to print it as a pdf on my own lap top
#Andrew more or less randomly chose html2pdf.app in order to
#demonstrate the technique
#of a live interaction with a separate website.
import requests
import json
################
#In this lab we are going to use Python access APIs that need a key
#We are using the APIs as described by:
#• https://html2pdf.app/
#• https://developer.github.com/v3/guides/
#######################################

#he registered with the website 
#then received an API key and sample curl code in a reply
#html = '<h1>hello world</h1>This is html'
f = open("../Week2/carviewer2.html", "r")
html = f.read()
print (html)
#########################
#That would be handy if you wanted to copy some beautiful pre-existing Code

#######################