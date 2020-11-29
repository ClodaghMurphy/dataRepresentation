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
from BookDAO import bookDao



@app.route('/')
def index():
   return  "is this thing on?"

@app.route('/books')
def getAll():
   #return  "this means the getAll() function was called"
   return jsonify(bookDao.getAll())
#curl http://127.0.0.1:5000/books

@app.route('/books/<int:ISBN>') 
def findById(ISBN): 
    return jsonify(bookDao.findById(ISBN))
#λ curl http://127.0.0.1:5000/books/123
#λ curl http://127.0.0.1:5000/books/19456
#λ curl http://127.0.0.1:5000/books/7777777

#curl -X POST -d "{\"ISBN\":1289, \"title\":\"new Title\", \"author\":\"John Irving\", \"price\":999}" -H "Content-Type:application/json" http://127.0.0.1:5000/books
#curl -X POST -d "{\"ISBN\":444, \"title\":\"new Title\", \"author\":\"John Irving\", \"price\":999}" -H "Content-Type:application/json" http://127.0.0.1:5000/books 
                                                                                                                                                                    
@app.route('/books', methods=['POST'])
def create(): 

    if not request.json: #abort the request if it is not in the correct json format
        abort(400)
    #if it is a good request do this, append the book with a new isbn and so on
    book = {
        "ISBN": request.json["ISBN"],
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }

    return jsonify(bookDao.create(book))
    #return "this means the create() function was called "



#@app.route('/books/<int:id>', methods=['PUT'])
#def update(id):
#   return  "this means the update(id) function was called "+ str(id)


#λ curl -X PUT -d "{\"title\":\"new1 Title\", \"price\":999}" -H "Content-Type:application/json" http://127.0.0.1:5000/books/123
#λ curl -X PUT -d "{\"title\":\"new1 Title\", \"price\":888}" -H "Content-Type:application/json" http://127.0.0.1:5000/books/1456
#if you don't enter a valid isbn you get a blank back like this{}
@app.route('/books/<int:ISBN>', methods=['PUT'])
def update(ISBN):
    foundBook=bookDao.findById(ISBN)
    print(foundBook)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'title' in request.json:
        currentBook['title'] = request.json['title']
    if 'author' in request.json:
        currentBook['author'] = request.json['author']
    if 'price' in request.json:
        currentBook['price'] = request.json['price']
    bookDao.update(currentBook)
    return jsonify(currentBook)

#@app.route('/books/<int:id>', methods=['DELETE'])
#def delete(id):
#   return  "this means the delete(id) function was called with id  "+ str(id)
#λ curl -X DELETE http://127.0.0.1:5000/books/1
#{
#  "done": true
#}

@app.route('/books/<int:ISBN>', methods=['DELETE'])
def delete(ISBN):
    bookDao.delete(ISBN)
#curl -X DELETE http://127.0.0.1:5000/books/12345
#if you put in an incorrect ISBN it still tellsyou that it worked 
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)