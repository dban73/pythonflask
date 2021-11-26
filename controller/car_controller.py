from flask import request, jsonify
import server
import db
from entity.car_entity import Car

# CREATE POST


def car_create():
    json = request.json
    car = Car(**json)
    db.Session.add(car)
    db.Session.commit()
    return jsonify(
        status="success",
        data=json
    )

# READ


def car_read(id):
    car = db.Session.query(Car).get(id)
    return jsonify(
        status="success",
        data=car.to_dict()
    )

# READ


def cars_read():
    cars = db.Session.query(Car).all()
    return jsonify(
        status="success",
        data=[car.to_dict() for car in cars]
    )

# UPDATE


def car_update(id):
    json = request.json
    car = db.Session.query(Car).get(id)
    for key, value in json.items():
        if hasattr(car, key):
            setattr(car, key, value)
    return jsonify(
        status="success",
        data=car.to_dict()
    )

# DELETE


def car_delete(id):
    car = db.Session.query(Car).get(id)
    db.Session.detete(car)
    db.Session.commit()
    return json(
        status="success",
        data=car.to_dict()
    )
