# Ambiente de Desenvolvimento

Aqui está organizado o monorepositório do projeto integrador,
juntando o banco de dados, o back-end e front-end

# Como usar

## Bando de dados

Para todos termos o mesmo ambiente de desenvolvimento,
o banco de dados com docker, será de grande auxilio para testar
e desenvolver junto.

[Instale o docker](https://docs.docker.com/engine/install/)

Execute o comando para subir o ambiente

```
docker-compose up
```

Após reiniciar o docker, pode ocorrer problemas, então remova a pasta

```
sudo rm -rf postgres-data/
```

E remova o volume criado pelo docker

```
docker-compose down -v
```

### Testar o Banco de dados

Utilize uma ferramenta gratuita chamada [Dbeaver CE](https://dbeaver.io/download/)

Crie a conexao no Dbeaver, no botao +

![start](/dev/img/new.png)

Selecione Dbeaver

![start](/dev/img/post.png)

Coloque as configurações

![start](/dev/img/conf.png)

username: admin

password: admin

Depois só ver os dados recem inseridos

![start](/dev/img/exemplo.png)

## Criando tabelas

Para criar tabelas existe o arquivo:

[Criar tabela](/dev/db/sql/create_tables.sql)

```sql
-- Creation of product table
CREATE TABLE IF NOT EXISTS tb_client_id (
  ID  SERIAL PRIMARY KEY,
  first_name varchar(250) NOT NULL,
  last_name varchar(450) NOT NULL,
  email varchar(250) NOT NULL,
  pass varchar(250) NOT NULL
);
```

Adicione novas tabelas neste padrão SQL.

## Adicionando dados

Para inserir dados na tabela criada, existe o arquivo:

[Inserir dados na tabela](/dev/db/sql/fill_tables.sql)

```sql
-- Filling of tb_client_id
INSERT INTO tb_client_id
(first_name, last_name, email, pass)
values
('Andre', 'da Silva', 'andre@exemplo.com', 'andre');
```