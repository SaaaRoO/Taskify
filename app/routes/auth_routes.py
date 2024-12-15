from flask import Blueprint, request, jsonify
from models.models import User
from db.database import db
from utils.jwt_utils import generate_token
from flask_jwt_extended import jwt_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = generate_token(username)
    return jsonify({"access_token": access_token}), 200
