#run this script to WRITE a new file containing your data{} in a json stylee called simple.json
import json

data =  {
    'name':'joe',
    'age':21,
    "student": True#different types of quotes, python doesn't mind.
    }
#print(data)

file = open("simple.json",'w')
json.dump(data,file, indent=4)#indent makes it look nicer (new lines) handy when using large quantities
