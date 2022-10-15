# *Back-end* do projeto Integrador

## Ferramentas
* Framework: [**Flask**](https://flask.palletsprojects.com/en/2.2.x/)
* Banco de Dados: [**PostgreSQL**](https://www.postgresql.org/)
* Teste de API: [**Postman**](https://www.postman.com/)


# Como utilizar

Ambiente virtual para desenvolvimento da aplicação em Flask
```bash
# Diretório para executar os seguintes comandos:
~/univesp_comp_pi3/dev/back $

# Criação do ambiente virtual
 virtualenv -p python3 env
# ou
python3 -m venv env


## Ativar o ambiente virtual 
source env/bin/activate


## Instalar requisitos 
pip3 install -r requirements.txt
```


Container (*Docker*) para banco de dados

```bash
# Diretório para executar os seguintes comandos:
~/univesp_comp_pi3/dev $

#Execute o comando para subir o ambiente
docker-compose up
# ou 
docker compose up


# Após reiniciar o docker, pode ocorrer problemas, então remova a pasta
sudo rm -rf postgres-data/

# E remova o volume criado pelo docker
docker-compose down -v
# ou
docker compose down -v

```

| Figura 1: Carregando o Banco de dados com Docker|
|:-----:|
|![Docker](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/4cdd3d0991841dc3b6a194a156f83b62c5ac0caf/dev/back/img/gif/01-docker_compose_up.gif)|
| Fonte: Próprio autor |


| Figura 2: Carregando Ambiente Virtual|
|:-------------------:|
|![Virtual environment](dev/back/img/gif/02-source_env_bin_activate.gif)|
|Fonte: Próprio autor |


| Figura: |
|:-------------------:|
||
|Fonte: Próprio autor |