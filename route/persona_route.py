from flask import request, jsonify
import server
from controller import persona_controller
#from controller import cliente_controller

# CREATE


@server.app.route('/personas', methods=['POST'])
def persona_create():
    return persona_controller.persona_create()

# READ


@server.app.route('/personas/<id>', methods=['GET'])
def persona_read(id):
    return persona_controller.persona_read(id)

# READ


@server.app.route('/personas', methods=['GET'])
def personas_read():
    return persona_controller.personas_read()

# UPDATE


@server.app.route('/personas/<id>', methods=['PUT', 'PATCH'])
def persona_update(id):
    return persona_controller.persona_update(id)

# DELETE


@server.app.route('/personas/<id>', methods=['DELETE'])
def persona_delete(id):
    return persona_controller.persona_delete(id)
