from flask import request, jsonify
import server
from controller import car_controller
#from controller import cliente_controller

# CREATE


@server.app.route('/cars', methods=['POST'])
def car_create():
    return car_controller.car_create()

# READ


@server.app.route('/cars/<id>', methods=['GET'])
def car_read(id):
    return car_controller.car_read(id)

# READ


@server.app.route('/cars', methods=['GET'])
def cars_read():
    return car_controller.cars_read()

# UPDATE


@server.app.route('/cars/<id>', methods=['PUT', 'PATCH'])
def car_update(id):
    return car_controller.car_update(id)

# DELETE


@server.app.route('/cars/<id>', methods=['DELETE'])
def car_delete(id):
    return car_controller.car_delete(id)
