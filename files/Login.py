from flask_restful import Resource
from flask import request
from templates import db, User

class Login(Resource):
  
    def post(self):
        records = request.get_json(force=True)
        if not records:
            return {'message' : 'No input data provided'}, 400

        user = User.query.filter_by(username=records['username']).first()

        if 'username' not in records or 'password' not in records:
            return {'message': 'Input data must contain a username and a password'}, 400    

        
        if user.password != records['password']:
            if user.failed_attempts is None:
                user.failed_attempts = 1
            else:
                user.failed_attempts += 1
            if user.failed_attempts >= 3:
                user.is_locked = True
            db.session.commit()
            return {'message': 'Something went wrong, please try again! '}, 400



        result = User.convert_to_json(user)
        return {'status' : 'success', 'data' : result}, 201
