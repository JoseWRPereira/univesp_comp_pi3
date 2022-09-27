from flask import Flask
from app.database.db import DBConn
# from api.auth import auth
# from api.test import test_bp
from app.api.auth import auth
from app.api.users import users_bp

app = Flask(__name__)
app.register_blueprint(users_bp)


@app.route("/")
def index():
    db = DBConn()
    lst = db.sql_fetch("SELECT * FROM tb_client_id;")
    return "Projeto Integrador 3 - {}".format( lst )

if __name__=="__main__":
    app.run()
