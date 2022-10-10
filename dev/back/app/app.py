# from flask import Flask

from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps


from app.database.db import DBConn
# from app.api.auth import auth
from app.api.users import users_bp
from app.api.auth import auth_login




app = Flask(__name__)
app.config['SECRET_KEY'] = 'Projeto Integrador III'
app.register_blueprint(users_bp)


@app.route("/")
def index():
    db = DBConn()
    lst = db.sql_fetch("SELECT * FROM tb_client_id;")
    return "Projeto Integrador 3 - {}".format( lst )







def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs ):
        token = request.args.get('token')
        print( '>>> Token >>> ')
        print( token )
        if not token:
            return jsonify({'message':'Token is missing'}),403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'Token is invalid'}),403
        
        return f(*args, **kwargs)
    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message':'Anyone can view this!'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message':'This is only available for peaple with valid tokens.'})


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        print('login'+auth.username)
        print('login'+str(datetime.datetime.utcnow()))
        payload = {'user':auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=60)}
        print("###")
        print(app.config['SECRET_KEY'])
        token = jwt.encode( payload, app.config['SECRET_KEY'])
        return jsonify({'token' : token})
    return make_response('Could not verify!', 401,{'WWW-Authenticate':'Basic Realm="Login Required"'})





if __name__=="__main__":
    app.run()
