from crypt import methods
from flask import Flask, jsonify, request, make_response
from app.database.db import DBConn
from app.api.users import users_bp
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # Cors para poder ser utilizado reactjs com front
app.config['SECRET_KEY'] = 'Projeto Integrador III'
app.register_blueprint(users_bp)


@app.route("/",methods=['GET'])
def index():
    return jsonify({"Projeto":"Integrador 3"})



if __name__=="__main__":
    app.run()
