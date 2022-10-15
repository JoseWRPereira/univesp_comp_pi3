from flask import Blueprint
from flask import request, json, jsonify
from flask_restful import Resource, Api
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db import DBConn
from .auth import auth_required
import datetime

users_bp = Blueprint('users_bp',__name__)
api = Api(users_bp)


header = ('Id','public_id','username','email','password','creation_date','last_access','admin')
fields = 'Id,public_id,username,email,password,creation_date,last_access,admin'
table = 'tb_users_id'




class Users(Resource):
    # @auth_required
    def get(self):
        db = DBConn()
        user_exists = db.sql_fetch("SELECT {} FROM {};".format(fields,table))
        dicio = []
        for user in user_exists:
            dicio.append(dict(zip(header,user)))
        response = {'users':dicio}
        # response = make_response( jsonify(dicio), 200 )
        # response.headers["Content-Type"] = "application/json"
        return jsonify(response)


    def post(self):
        dados = request.get_json()
        db = DBConn()
        user_exists = db.sql_fetch("SELECT email,password FROM {} WHERE email='{}';".format(table,dados['email']))
        if not user_exists:
            db.sql_cmd("INSERT INTO {} (public_id,username,email,password,creation_date,last_access,admin)\
                        VALUES ('{}','{}','{}','{}','{}','{}',{});".format(
                            table,
                            uuid.uuid4(), 
                            dados['username'],
                            dados['email'],
                            generate_password_hash(dados['password'], method='sha256'),
                            datetime.date.today(),
                            datetime.datetime.today(),
                            False ))
            mensagem = "Usuário com e-mail {} criado com sucesso!".format(dados['email'])
            response = {"Status": "Sucesso", "message": mensagem }
        else:
            mensagem = "Usuário com e-mail {} já está cadastrado!".format(dados['email'])
            response = {"Status": "erro", "message": mensagem }
        return jsonify(response)


class User(Resource):
    @auth_required
    def get(self, public_id):
        try:
            db = DBConn()
            user_exists = db.sql_fetch("SELECT {} FROM {} WHERE public_id='{}';".format(fields, table, public_id))
            response = {'user':dict( zip(header, user_exists.pop()))}
        except IndexError:
            message = "Usuário com ID público {} não existe!".format(public_id)
            response = {"Status": "erro", "message": message }
        except Exception:
            message = "Erro desconhecido. Procure o administrador da API!"
            response = {"Status": "erro", "message": message }
        return jsonify(response)

    # @auth_required
    def put(self, public_id):
        try:
            db = DBConn()
            user_exists = db.sql_fetch("SELECT {} FROM {} WHERE public_id='{}';".format(fields, table, public_id))
            user = dict( zip(header, user_exists.pop()))
            dados = json.loads(request.data)
            if check_password_hash(user['password'], dados['password']):
                db.sql_cmd("UPDATE {} \
                    SET username='{}',email='{}',last_access='{}' \
                    WHERE public_id='{}';".format( 
                            table,
                            dados['username'],dados['email'],datetime.datetime.today(),
                            public_id ))

                user_exists = db.sql_fetch("SELECT {} FROM {} WHERE public_id='{}';".format(fields, table, public_id))
                response = {'user':dict( zip(header, user_exists.pop()))}
            else:
                response = {"Status":"erro", "message":"Senha inválida!"}
        except IndexError:
            message = "Usuário com ID público {} não existe!".format(public_id)
            response = {"Status": "erro", "message": message }
        except Exception:
            message = "Erro desconhecido. Procure o administrador da API!"
            response = {"Status": "erro", "message": message }
        return jsonify(response)

    
    # @auth.login_required
    def delete(self, public_id):
        try:
            db = DBConn()
            user_exists = db.sql_fetch("SELECT {} FROM {} WHERE public_id='{}';".format(fields, table, public_id))
            if not user_exists:
                response = {'Status':'Erro', 'message':'Registro não existe!'}
            else:
                db.sql_cmd("DELETE FROM {} WHERE public_id='{}';".format(table,public_id) )
                response = {'Status':'Sucesso', 'message':'Usuário excluído.'}
        except IndexError:
            message = "Usuário com ID público {} não existe!".format(public_id)
            response = {"Status": "erro", "message": message }
        except Exception:
            message = "Erro desconhecido. Procure o administrador da API!"
            response = {"Status": "erro", "message": message }
        return jsonify(response)


api.add_resource(Users,'/api/users')
api.add_resource(User,'/api/user/<public_id>')

@users_bp.route('/api')
def api():
    _routes_ = ['/api/users','/api/user/<public_id>']
    _api_ = {'routes':_routes_}
    return jsonify({"API": _api_ })
