from flask import request, jsonify
import server,db
from entity.persona_Entity import Persona

#CREATE POST
def persona_create():
    json = request.json
    persona = Persona(**json)
    db.Session.add(persona)
    db.Session.commit()
    return jsonify(
        status = "success",
        data = json
    )

#READ
def persona_read(id):
    persona = db.Session.query(Persona).get(id)
    return jsonify(
        status = "success",
        data = persona.to_dict()
    )

#READ
def personas_read():
    personas = db.Session.query(Persona).all()
    return jsonify(
        status = "success",
        data = [persona.to_dict() for persona in personas]
    )

#UPDATE     
def persona_update(id):
    json = request.json
    persona = db.Session.query(Persona).get(id)
    for key, value in json.items():
        if hasattr(persona, key):
            setattr(persona, key, value)
    return jsonify(
        status = "success",
        data = persona.to_dict()
    )

#DELETE
def persona_delete(id):
    persona = db.Session.query(Persona).get(id)
    db.Session.detete(persona)
    db.Session.commit()
    return json(
        status = "success",
        data = persona.to_dict()
    )