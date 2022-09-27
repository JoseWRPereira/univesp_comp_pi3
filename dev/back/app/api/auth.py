from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db import DBConn

auth = HTTPBasicAuth()


users = {
    'jose': generate_password_hash('jose'),
    'william': generate_password_hash('william')
}


@auth.verify_password
def verify_password(username, password):
    # db = DBConn()
    # lst = db.sql_fetch("SELECT (id, email, pass) from tb_users_id;")

    if username in users and \
            check_password_hash(users.get(username), password):
        return username
