from flask import request,Flask,jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity


# app.config['JWT_SECRET_KEY'] = 'super-secret'
# jwt = JWTManager(app) 

class Userregistration(Resource):
	def post(self):
		username = request.json.get('username', None)
		password = request.json.get('password', None)
		if not username:
			return jsonify({"message":"Enter username"}), 400
		if not password:
			return jsonify({"message":"Enter password"}), 400

		if username != 'admin' or password !='admin':
			return jsonify({"message":"Can't login"}),401

		access_token = create_access_token(identity=username)
		return jsonify(access_token=access_token),200

