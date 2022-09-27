from flask import Flask
from app.database.db import DBConn

app = Flask(__name__)

@app.route("/")
def index():
    db = DBConn()
    lst = db.sql_fetch("SELECT * FROM tb_client_id;")
    return "Projeto Integrador 3 - {}".format( lst )



if __name__=="__main__":
    app.run()
