#+++++++RUNNING INSTRUCTIONS++++++++
#either server.py OR
# SET FLASK_APP=server
# echo %FLASK_APP%
#(now flask run will work!)
from flask import Flask, url_for, request, redirect, abort
#url_for otherwise that app won't work
#request to get your data import request object see also week 5code
#redirect seamlessly redirects them to another url
#abort  not executed
#ON BROWSER- http://127.0.0.1:5000/test.html
app = Flask(__name__, static_url_path='', static_folder='staticpages')
@app.route('/')
def index():
   return  redirect(url_for('login'))#ifthey go to "/", force them to login
#Pass the url MAPPING andlocation of the static pages when creating the app


@app.route('/login')
def login():
    abort(401)
    return "served by Login"

@app.route('/user')#map get method to /user URL
def getUser():
    return "served by getUser"#just helps you know what function is the source

@app.route('/user/<int:id>')#set a variable in url of type int called id
#Integers can map to strings, but strings cannot map to integers
#Test like this on browser http://127.0.0.1:5000/user/568
#served by findByIdUser with id = 568
#When you try to find with the wrong type of data class (string instead of an integer)
#http://127.0.0.1:5000/user/clodagh
#The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
def findByIdUser(id):
    return "served by findByIdUser with id = "+str(id)#




#mapping of a function or a post method
#this (post) can't be tested by just looking at the browser, so you need to use CURL instead
# CURL http://127.0.0.1:5000/user
#served by getUser
#λ CURL -X POST http://127.0.0.1:5000/user
#served by createUser
@app.route('/user', methods=['POST'])
def createUser():
    return "served by createUser"

@app.route("/demo_url_for")
#this is when you need to generate a url for a particular function
#TEST like this http://127.0.0.1:5000/demo_url_for
#url For index is /
#url for findByIdUser /user/12
def demoUrlFor():
    returnString = "url For index is "+ url_for('index')
    returnString += "<br/>"
    returnString += "url for findByIdUser "+ url_for('findByIdUser', id=12)#doesn't work without passing one in.
    return returnString

@app.route("/demo_request", methods=['POST', 'GET', 'DELETE'])
#TEST in the browser http://127.0.0.1:5000/demo_request
#It tells you what method was used to carry out the request
#TEST on command line
#λ CURL -X POST http://127.0.0.1:5000/demo_request
#POST
#λ CURL -X DELETE http://127.0.0.1:5000/demo_request
#DELETE
#λ CURL -X PUT http://127.0.0.1:5000/demo_request
#<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
#<title>405 Method Not Allowed</title>
#<h1>Method Not Allowed</h1>
#<p>The method is not allowed for the requested URL.</p>
def demoRequest():
    return request.method

if __name__ == "__main__":
    print("to see the two methods, this one is when you call server.py instead of set flask app=server then flask run version")
#two ways to run flask server, server.py or open the flask app
    app.run(debug=True)