#Where a html doc made in a previous week is converted to a pdf
#that is not a big deal in itself e.g.I could chose to print it as a pdf on my own lap top
#Andrew more or less randomly chose html2pdf.app in order to
#demonstrate the technique
#of a live interaction with a separate website.
import requests
import json


#he registered with the website 
#then received an API key and sample curl code in a reply
#html = '<h1>hello world</h1>This is html'
f = open("../Week2/carviewer2.html", "r")
html = f.read()
#print (html)
#provided by the API resource owner (html2pdf)
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)
print (response.status_code)

newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)