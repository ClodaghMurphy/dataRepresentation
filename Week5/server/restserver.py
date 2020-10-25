#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')
#the part where cars data is saved in memory but as soon as the program ends, the memory is lost.
#an array or list is made for storing the cars
cars = [
    {
        "reg":"181 G 1234",
        "make":"Ford",
        "model":"Modeo",
        "price":18000
    },
    {
        "reg":"11 MO 1234",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    },
    {
        "reg":"test",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    }
]

@app.route('/cars', methods=['GET'])#url map for /cars for method GET only
def get_cars():
    return jsonify( {'cars':cars})#returns the list converted in json
# curl -i http://localhost:5000/cars

@app.route('/cars/<string:reg>', methods =['GET'])
#anything with cars/something and method GET will be handled by this method
#the something (other search parameter) will be passed into the function as a string called reg
def get_car(reg):#how to get cars
    foundCars = list(filter(lambda t : t['reg'] == reg , cars))
#this is a filter that searches through the list of entries in cars and returns
#those matching the reg variable
    if len(foundCars) == 0:
#if nothing is returned, send back an empty or blank car with status 204
        return jsonify( { 'car' : '' }),204
    return jsonify( { 'car' : foundCars[0] })#else return first of the found cars (counting starts at 0!)
#curl -i http://localhost:5000/cars/test

@app.route('/cars', methods=['POST'])#post method innit
def create_car():#the reg query #find by id 
    if not request.json:
        abort(400)#if the request does not have JSON data, return 400 error
    if not 'reg' in request.json:
        abort(400)
    car={#reads request object to create a new car
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price']
    }
    cars.append(car)#append the request object to the list of cars
    return jsonify( {'car':car }),201#return information of what was just added
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# for windows use this one
#this is a code that can be input at the cmd to create or post a new record onto the cars database
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg\":\"12 D 666\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}" http://localhost:5000/cars
@app.route('/cars/<string:reg>', methods =['PUT'])#PUt takes in reg from the URL
def update_car(reg):#the part to update
    foundCars=list(filter(lambda t : t['reg'] ==reg, cars))#filter to find the car
    if len(foundCars) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'make' in request.json and type(request.json['make']) != str:#check json in request formatted correctly
        abort(400)
    if 'model' in request.json and type(request.json['model']) is not str:#if string is wrong
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:#if it's not an int
        abort(400)
    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
    return jsonify( {'car':foundCars[0]})#return the found car
    #handy when ids are controlled by the server (not the client)
#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234

@app.route('/cars/<string:reg>', methods =['DELETE'])
def delete_car(reg):#section for deleting items
    foundCars = list(filter (lambda t : t['reg'] == reg, cars))
    if len(foundCars) == 0:
        abort(404)#not found = 404
    cars.remove(foundCars[0])#remove the found car from list of cars
    return  jsonify( { 'result':True })#output
#error handling 400 and 404 is down here
#they return simple JSON
#but comment them out when you are debugging because
#it will prevent you seeing all the errors
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)
