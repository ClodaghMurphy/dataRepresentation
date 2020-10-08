from bs4 import BeautifulSoup

with open("../Week2/carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')#fp = file pointer

#print (soup.tr)
#above command is commented out but it finds the first instance of a tr
rows = soup.findAll("tr")#find all of the elements called tr
for row in rows:
    #print("-------")
    #print(row)# the 3 preceeding lines would print out every instance of tr tags in turn
    dataList = []#tostore in a list
    #note the first line is an empty pair of brackets!
    cols = row.findAll("td")
    #command to find all the td tags
    for col in cols:
        dataList.append(col.text)
    print (dataList)