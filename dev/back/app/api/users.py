from flask import Blueprint
from flask import request, json, jsonify, make_response
from flask_restful import Resource, Api
from app.api.auth import auth
from app.database.db import DBConn

users_bp = Blueprint('users_bp',__name__)
api = Api(users_bp)

equipe = [
    {   'id':0, 
        'nome':'José', 
        'cargo':'Programador' 
    },
    {   'id':1, 
        'nome':'William', 
        'cargo':'Cientista de dados' 
    }
]

class Users(Resource):
    # @auth.login_required
    def get(self):

        db = DBConn()
        users = db.sql_fetch("SELECT id,first_name,last_name,email,pass from tb_users_id;")
        header = ["id", "first_name", "last_name", "email", "pass"]

        dicio = []
        for user in users:
            dicio.append( dict( zip(header, user)) )

        response = make_response( jsonify(dicio), 200 )
        response.headers["Content-Type"] = "application/json"
        return response


    def post(self):
        db = DBConn()
        users = db.sql_fetch("SELECT id,first_name,last_name,email,pass from tb_users_id;")
        header = ["id", "first_name", "last_name", "email", "pass"]
        dicio = []
        if users == dicio:
            posicao = 1
        else:
            for user in users:
                dicio.append( dict( zip(header, user)) )
            posicao = len(dicio)+1
        dados = json.loads(request.data)
        dados['id'] = posicao
        db.sql_cmd("INSERT INTO tb_users_id (id,first_name,last_name,email,pass) VALUES ('{}','{}','{}','{}','{}');".format(
                    dados['id'],
                    dados['first_name'],
                    dados['last_name'],
                    dados['email'],
                    dados['pass']))
        return dados


class User(Resource):
    # @auth.login_required
    def get(self, id):
        try:
            response = equipe[id]
        except IndexError:
            mensagem = "Tarefa com ID {} não existe!".format(id)
            response = {"status": "erro", "mensagem": mensagem }
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API!"
            response = {"status": "erro", "mensagem": mensagem }
        return response

    def put(self, id):
        dados = json.loads(request.data)
        equipe[id] = dados
        return dados
    
    def delete(self, id):
        equipe.pop(id)
        return {'status':'Sucesso', 'mensagem':'Registro excluído'}






api.add_resource(Users,'/users')
api.add_resource(User,'/user/<int:id>')

@users_bp.route('/api')
def api():
    return "API Blueprint"


