import psycopg2
import psycopg2.extras
from psycopg2 import Error


#########################################
# Parâmetros de conexão com banco de dados Postgres local
#########################################
DB_HOST = '127.0.0.1'
DB_DATABASE = 'integrador'
DB_USER = 'admin'
DB_PORT = '5432'
DB_PASSWORD = 'admin'

DB_URI = "postgres://{}:{}@{}:{}/{}".format(
                    DB_USER,
                    DB_PASSWORD,
                    DB_HOST,
                    DB_PORT,
                    DB_DATABASE)

#########################################
######################################### DBConn

class DBConn():
    def __init__(self):
        self.host = DB_HOST
        self.database = DB_DATABASE
        self.user = DB_USER
        self.port = DB_PORT
        self.password = DB_PASSWORD
        self.uri = DB_URI


    def sql_fetch(self, sql):
        try:
            connection = psycopg2.connect( self.uri )
            cursor = connection.cursor()
            cursor.execute(sql)
            print("SQL FETCH: ", sql, "\n")
            lista = cursor.fetchall()
            for l in lista:
                print("  ", l, "\n")
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL: ", error)
            cursor.execute("ROLLBACK;")
            lista = []
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
                return lista


    def sql_cmd(self, sql):
        try:
            connection = psycopg2.connect(  database=self.database,
                                            user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            port=self.port
                                        )
            cursor = connection.cursor()
            cursor.execute(sql)
            print("SQL CMD: ", sql, "\n")
            cursor.execute("COMMIT;")
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL: ", error)
            cursor.execute("ROLLBACK;")
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


#########################################
#########################################
