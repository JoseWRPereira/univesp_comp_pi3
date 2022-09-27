### crud.py ###

from sqlalchemy import create_engine

DATABASE_URI = 'postgresql+psycopg2://admin:admin@localhost:5432/integrador'

engine = create_engine(DATABASE_URI)
with engine.connect() as connection:
    SQL = "select * from tb_client_id;"
    result = connection.execute(SQL)
    for row in result:
        print(row)

if __name__ == '__main__':
    print("END")