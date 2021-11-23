from flask import request, jsonify
import server
#from controller import cliente_controller

#CREATE
@server.app.route('/personas', methods=['POST'])
def persona_create():
    return "persona_controller.persona_create()"

#READ
@server.app.route('/personas/<id>', methods=['GET'])
def persona_read(id):
    return "persona_controller.persona_read(id)"

#READ
@server.app.route('/personas', methods=['GET'])
def personas_read():
    return "API GET PERSONAS"
   # return "persona_controller.persona_read()"

#UPDATE 
@server.app.route('/personas/<id>', methods=['PUT','PATCH'])
def persona_update(id):
    return "persona_controller.persona_update(id)"

#DELETE
@server.app.route('/personas/<id>', methods=['DELETE'])
def persona_delete(id):
    return "persona_controller.persona_delete(id)"