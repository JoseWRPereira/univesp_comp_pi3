from flask import Flask, request, make_response
from functools import wraps
from werkzeug.security import check_password_hash
from app.database.db import DBConn


def user_auth_by_email(username):
    try:
        db = DBConn()
        user_exists = db.sql_fetch("SELECT email,pass FROM tb_users_id WHERE email='{}';".format(username))
        header = ('username','password')
        return dict( zip(header, user_exists.pop()))
    except:
        return None


def auth_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth = request.authorization
        if auth:
            user = user_auth_by_email(auth.username)
        if auth and user and auth.username == user['username'] and check_password_hash( user['password'], auth.password):
            return f(*args,**kwargs)
        return make_response('Could not verify your login!', 401,{'WWW-Authenticate':'Basic realm="Login Required"'})
    return decorated

