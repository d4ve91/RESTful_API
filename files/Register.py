from flask_restful import Resource
from flask import request
from templates import db, User
import secrets
import hashlib

class Register(Resource):
    def get(self):
        username = request.args.get('username')
        emailadress = request.args.get('emailadress')
        role = request.args.get('role')

        users = User.query.all()
        if username:
            users = users.filter_by(username=username)
        if emailadress:
            users = users.filter_by(email=emailadress)
        if role:
            users = users.filter_by(role=role)

        user_list = []
        for user in users:
            user_list.append(user.serialize())
        return {'positions' : str(user_list)}, 200

    
    def post(self):
        records = request.get_json(force=True)
        
        password = records['password'].encode('utf-8')
        salt = secrets.token_hex(16)
        salted_password = salt.encode('utf-8') + password
        hashed_password = hashlib.sha256(salted_password).hexdigest()

        
        if not records or 'username' not in records or 'emailadress' not in records:
            return {'message' : 'No input data provided'}, 400

        if not 3 <= len(records['username']) <= 32:
           return {'message' : 'Username must be between 3 and 32 characters long'}, 400

        if not all(c.isalnum() or c == '_' for c in records['username']):
            return {'message' : 'Username can only contain alphanumeric characters or underscores'}, 400

        user = User.query.filter_by(username=records['username']).first()
        if user:
            return {'message' : 'User with the same username already exists'}, 400

        if not 8 <= len(records['password']) <= 100:
           return {'message' : 'The password must contain more than 8 characters'}, 400

        if '@' not in records['emailadress'] or '.' not in records['emailadress']:
            return {'message' : 'Invalid email address'}, 400

        user = User.query.filter_by(emailadress=records['emailadress']).first()
        if user:
            return {'message' : 'Email already exists'}, 400

        try:
            failed_attempts = records['failed_attempts']
        except KeyError:
            failed_attempts = 0


        
        user = User(
            
            firstname = records['firstname'], 
            lastname = records['lastname'], 
            emailadress = records['emailadress'], 
            password = hashed_password, 
            username = records['username'], 
            failed_attempts = failed_attempts,

        )
        db.session.add(user)
        db.session.commit()

        result = User.serialize(user)
        return {'status' : 'success', 'data' : result}, 201