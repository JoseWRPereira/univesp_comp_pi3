from flask import Blueprint
from flask import request, json, jsonify, make_response
from flask_restful import Resource, Api
from app.api.auth import auth
from app.database.db import DBConn

users_bp = Blueprint('users_bp',__name__)
api = Api(users_bp)


class Users(Resource):
    # @auth.login_required
    def get(self):
        db = DBConn()
        users = db.sql_fetch("SELECT id,first_name,last_name,email,pass from tb_users_id ORDER BY id ASC;")
        header = ["Id", "first_name", "last_name", "email", "pass"]

        dicio = []
        for user in users:
            dicio.append( dict( zip(header, user)) )

        response = make_response( jsonify(dicio), 200 )
        response.headers["Content-Type"] = "application/json"
        return response

    def post(self):
        db = DBConn()
        dados = json.loads(request.data)
        db.sql_cmd("INSERT INTO tb_users_id (\
                        first_name,last_name,email,pass) \
                    VALUES ('{}','{}','{}','{}');".format(
                        dados['first_name'],
                        dados['last_name'],
                        dados['email'],
                        dados['pass']))
        user = db.sql_fetch("SELECT id,first_name,last_name,email,pass \
                                FROM tb_users_id \
                                ORDER BY id \
                                DESC LIMIT 1;")
        header = ("Id", "first_name", "last_name", "email", "pass")
        dicio = []
        dicio.append( dict( zip(header, user[0])) )
        response = make_response( jsonify(dicio), 200 )
        response.headers["Content-Type"] = "application/json"
        return response


class User(Resource):
    # @auth.login_required
    def get(self, id):
        try:
            db = DBConn()
            user = db.sql_fetch("SELECT id,first_name,last_name,email,pass FROM tb_users_id WHERE id='{}';".format(id))
            header = ("id", "first_name", "last_name", "email", "pass")
            dicio = []
            if user != dicio:
                for u in user:
                    dicio.append( dict( zip(header, user[0])) )
                response = make_response( jsonify(dicio), 200 )
                response.headers["Content-Type"] = "application/json"
            else:
                mensagem = "Tarefa com ID {} não existe!".format(id)
                response = {"status": "erro", "mensagem": mensagem }
        except IndexError:
            mensagem = "Tarefa com ID {} não existe!".format(id)
            response = {"status": "erro", "mensagem": mensagem }
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API!"
            response = {"status": "erro", "mensagem": mensagem }
        return response

    def put(self, id):
        db = DBConn()
        dados = json.loads(request.data)
        dados['id'] = id
        db.sql_cmd("UPDATE tb_users_id\
            SET first_name = '{}', \
                last_name = '{}',\
                email = '{}',\
                pass = '{}' \
            WHERE id = '{}';".format( 
                    dados['first_name'],
                    dados['last_name'],
                    dados['email'],
                    dados['pass'],
                    dados['id'] ))
        return dados
    
    def delete(self, id):
        db = DBConn()
        user = db.sql_fetch("SELECT id,first_name,last_name,email,pass FROM tb_users_id WHERE id='{}';".format(id))
        if user:
            db.sql_cmd("DELETE FROM tb_users_id WHERE id='{}';".format(id) )
            return {'status':'Sucesso', 'mensagem':'Registro excluído'}
        else:
            return {'status':'Erro', 'mensagem':'Registro não existe!'}





api.add_resource(Users,'/users')
api.add_resource(User,'/user/<int:id>')

@users_bp.route('/api')
def api():
    return "API Blueprint"


