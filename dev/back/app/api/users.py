from flask import Blueprint
from flask import request, json, jsonify, make_response
from flask_restful import Resource, Api
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
# from app.api.auth import Auth, auth, Validate
from app.database.db import DBConn



users_bp = Blueprint('users_bp',__name__)
api = Api(users_bp)


class Users(Resource):
    # @auth.login_required
    def get(self):
        db = DBConn()
        users = db.sql_fetch("SELECT id,public_id, first_name,last_name,email,pass from tb_users_id ORDER BY id ASC;")
        header = ["Id", "public_id","first_name", "last_name", "email", "pass"]
        dicio = []
        for user in users:
            dicio.append( dict( zip(header, user)) )

        response = jsonify({'users':dicio})
        # response = make_response( jsonify(dicio), 200 )
        # response.headers["Content-Type"] = "application/json"
        return response


    # @auth.login_required
    def post(self):
        db = DBConn()
        # dados = request.get_json()
        dados = json.loads(request.data)
        # response = dados['email']
        public_id = uuid.uuid4()
        hashed_pass = generate_password_hash(dados['pass'], method='sha256')
        user_exists = db.sql_fetch("SELECT ID,public_id,first_name,last_name,email,pass from tb_users_id WHERE email='{}';".format(dados['email']))
        if not user_exists:
            db.sql_cmd("INSERT INTO tb_users_id (\
                            public_id,first_name,last_name,email,pass) \
                        VALUES ('{}','{}','{}','{}','{}');".format(
                            public_id,
                            dados['first_name'],
                            dados['last_name'],
                            dados['email'], 
                            hashed_pass ))
            response = jsonify({"status":"OK", "message":"Usuário {} criado com sucesso!".format(dados['email'])})
        else:
            mensagem = "Usuário com e-mail {} já está cadastrado!".format(dados['email'])
            response = {"status": "erro", "mensagem": mensagem }
            # header = ("Id", "first_name", "last_name", "email", "pass")
            # dicio = []
            # dicio.append( dict( zip(header, user_exists.pop() )) )
            # response = jsonify( dicio )
        # if exists==[]:
        #     db.sql_cmd("INSERT INTO tb_users_id (\
        #                     first_name,last_name,email,pass) \
        #                 VALUES ('{}','{}','{}','{}');".format(
        #                     dados['first_name'],
        #                     dados['last_name'],
        #                     dados['email'], 
        #                     hash(pwd) ))
        #     user = db.sql_fetch("SELECT id,first_name,last_name,email,pass \
        #                             FROM tb_users_id \
        #                             ORDER BY id \
        #                             DESC LIMIT 1;")
        #     header = ("Id", "first_name", "last_name", "email", "pass")
        #     dicio = []
        #     dicio.append( dict( zip(header, user[0])) )
        #     response = make_response( jsonify(dicio), 200 )
        #     response.headers["Content-Type"] = "application/json"
        # else:
        #     mensagem = "Usuário com e-mail {} já está cadastrado!".format(dados['email'])
        #     response = {"status": "erro", "mensagem": mensagem }
        return response


class User(Resource):
    def get(self, public_id):
        try:
            db = DBConn()
            user_exists = db.sql_fetch("SELECT id,public_id,first_name,last_name,email,pass FROM tb_users_id WHERE public_id='{}';".format(public_id))
            header = ("Id", "public_id", "first_name", "last_name", "email", "pass")
            dicio = []
            if not user_exists:
                mensagem = "Usuário com ID público {} não existe!".format(public_id)
                response = {"status": "erro", "mensagem": mensagem }
            else:
                dicio.append( dict( zip(header, user_exists.pop())) )
                response = jsonify(dicio)
                # for u in user:
                #     dicio.append( dict( zip(header, user[0])) )
                # response = make_response( jsonify(dicio), 200 )
                # response.headers["Content-Type"] = "application/json"
        except IndexError:
            mensagem = "Tarefa com ID {} não existe!".format(id)
            response = {"status": "erro", "mensagem": mensagem }
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API!"
            response = {"status": "erro", "mensagem": mensagem }
        return response

    # @auth.login_required
    def put(self, public_id):
        db = DBConn()
        user_exists = db.sql_fetch("SELECT id,public_id,first_name,last_name,email,pass FROM tb_users_id WHERE public_id='{}';".format(public_id))
        header = ("Id", "public_id", "first_name", "last_name", "email", "pass")
        dicio = []
        if not user_exists:
            mensagem = "Usuário com ID público {} não existe!".format(public_id)
            response = {"status": "erro", "mensagem": mensagem }
        else:
            dicio.append( dict( zip(header, user_exists.pop())) )

            dados = json.loads(request.data)
            user = dicio.pop()
            if check_password_hash(user['pass'], dados['pass']):
                # response = jsonify({'senha':user['pass']})
                dados['id'] = user['Id']
                dados['public_id'] = public_id
                hashed_pass = generate_password_hash(dados['pass'], method='sha256')
                db.sql_cmd("UPDATE tb_users_id\
                    SET first_name = '{}', \
                        last_name = '{}',\
                        email = '{}',\
                        pass = '{}' \
                    WHERE public_id = '{}';".format( 
                            dados['first_name'],
                            dados['last_name'],
                            dados['email'],
                            hashed_pass,
                            public_id ))
                response = jsonify(dados)
            else:
                response = jsonify({"status":"erro", "mensagem":"Senha inválida!"})
        return response
    
    # @auth.login_required
    def delete(self, public_id):
        db = DBConn()
        user_exists = db.sql_fetch("SELECT id,public_id,first_name,last_name,email,pass FROM tb_users_id WHERE public_id='{}';".format(public_id))
        if not user_exists:
            return jsonify({'status':'Erro', 'mensagem':'Registro não existe!'})
        else:
            db.sql_cmd("DELETE FROM tb_users_id WHERE public_id='{}';".format(public_id) )
            return {'status':'Sucesso', 'mensagem':'Registro excluído'}





api.add_resource(Users,'/users')
api.add_resource(User,'/user/<public_id>')

@users_bp.route('/api')
def api():
    return "API Blueprint"

# @users_bp.route('/api/validate/', methods=[GET, POST, PUT])
# def api_validate():
#     dados = json.loads(request.data)
#     return dados



