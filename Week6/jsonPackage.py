#run this script to print out your data{} in a json stylee.
import json

data =  {
    'name':'joe',
    'age':21,
    "student": True#different types of quotes, python doesn't mind.
    }
#print(data)

file = open("simple.json",'w')
#json.dump(data,file, indent=4)
jsonString = json.dumps(data)#dumps returns a string
print(jsonString)
#run this script to print out your data{} in a json stylee to the screen.