#This code is recycled from Lecture week 8
#+++++++RUNNING INSTRUCTIONS++++++++
#either server.py OR
# SET FLASK_APP=server
# echo %FLASK_APP%
#(now flask run will work!)

#url_for otherwise that app won't work
#request to get your data import request object see also week 5code
#redirect seamlessly redirects them to another url
#abort  not executed
#ON BROWSER- http://127.0.0.1:5000/test.html



from flask import Flask, url_for, request, redirect, abort,jsonify
app = Flask(__name__, static_url_path='', static_folder='staticpages')

books=[
    {"id":1, "Title":"Practival Node.js ", "Author": "Angela Mardan ", "Price":12},
    {"id":2, "Title":"Computer Organization and Architecture ", "Author": "Winona Stallings ", "Price":13},
    {"id":3, "Title":"The Single Vegan ", "Author": "Leah Leneman ", "Price":17}
]
nextId=4


@app.route('/')
def index():
   return  "is this thing on?"

@app.route('/books')
def getAll():
   #return  "this means the getAll() function was called"
   return jsonify(books)


@app.route('/books/<int:id>') 
def findById(id): 
    foundBooks = list(filter (lambda t : t["id"]== id, books))
#lambda function convert and filter the list of books, go through every object in the array
# id was passed in, books is the object
    #print(foundBooks)
    if len(foundBooks) == 0: #if ya find nothing with that id,  code 204 shows up on the server
        return jsonify({}) , 204
    return jsonify(foundBooks[0]) 



@app.route('/books', methods=['POST'])
def create(): 
    global nextId
    if not request.json: #abort the request if it is not in the correct json format
        abort(400)
    #if it is a good request do this, append the book with a new id and so on
    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    books.append(book)
    nextId += 1
    return jsonify(book)
    return "this means the create() function was called "

#@app.route('/books', methods=['POST'])
#def create():
#   return "this means the create() function was called" 

#@app.route('/books/<int:id>', methods=['PUT'])
#def update(id):
#   return  "this means the update(id) function was called "+ str(id)


@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if not request.json: #abort the request if it is not in the correct json formt
        abort(400)
    if len(foundBooks) == 0:#if ya find nothing with that id,  code 404 shows up on the server, {} on the screen.
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    return jsonify(currentBook)

#@app.route('/books/<int:id>', methods=['DELETE'])
#def delete(id):
#   return  "this means the delete(id) function was called with id  "+ str(id)


@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])

    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)