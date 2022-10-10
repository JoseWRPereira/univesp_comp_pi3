from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps
# from app import app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs ):
        token = request.args.get('token')

        if not token:
            return jsonify({'message':'Token is missing'})
        try:
            data = jwt.decode(token,app.config.get['SECRET_KEY'])
            # data = jwt.decode(token, "PI3Univesp")
        except:
            return jsonify({'message':'Token is invalid'})
        
        return f(*args, **kwargs)
    return decorated




def auth_login(secret_key):
    auth = request.authorization
    if auth and auth.password == 'password':
        print(auth.username)
        print(datetime.datetime.utcnow())
        # token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=5)}, app.config['SECRET_KEY'] )
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': auth.username
        }
        token = jwt.encode( payload, secret_key, algorithm = 'HS256')
        return token
    else:
        return make_response('Could not verify!', 401,{'WWW-Authenticate':'Basic Realm="Login Required"'})




# from flask_httpauth import HTTPBasicAuth
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask import jsonify
# from flask_restful import Resource
# from app.database.db import DBConn

# auth = HTTPBasicAuth()

# users = {
#     'jose': generate_password_hash('jose'),
#     'william': generate_password_hash('william')
# }


# @auth.verify_password
# def verify_password(username, password):
#     db = DBConn()
#     lst = db.sql_fetch("SELECT email,pass FROM tb_users_id WHERE email='{}';".format(username))
#     if lst==[]:
#         return False
#     else:
#         usr = '{}'.format(lst[0][0])
#         pwd = '{}'.format(lst[0][1])
#         hsh = hash(password)
#         print(usr)
#         print(pwd)
#         print(password)
#         print(hsh)
#         if pwd == hsh:
#             return True
#         else:
#             return False
