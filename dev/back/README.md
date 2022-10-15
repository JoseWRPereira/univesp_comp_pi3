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
|![Virtual environment](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/e3721e16acf4d2e239296fff14a410635fac69ab/dev/back/img/gif/02-source_env_bin_activate.gif)|
|Fonte: Próprio autor |


| Figura 3: Primeiro acesso via GET à tabela de usuários |
|:-------------------:|
|![GET users](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/e3721e16acf4d2e239296fff14a410635fac69ab/dev/back/img/gif/10-get_users.gif)|
|Fonte: Próprio autor |



| Figura 4: Novo usuário |
|:-------------------:|
|![Novo usuário](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/e3721e16acf4d2e239296fff14a410635fac69ab/dev/back/img/gif/11-post_newuser.gif)|
|Fonte: Próprio autor |


| Figura 5: Visualizando novo usuário |
|:-------------------:|
|![Visualizando novo usuário](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/e3721e16acf4d2e239296fff14a410635fac69ab/dev/back/img/gif/12-newuser_1.gif)|
|Fonte: Próprio autor |



| Figura 6: Adicionando usuário |
|:-------------------:|
|![Add usuário](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/e3721e16acf4d2e239296fff14a410635fac69ab/dev/back/img/gif/13-newuser2.gif)|
|Fonte: Próprio autor |



| Figura 7: Visualizando usuários no navegador |
|:-------------------:|
|![Usuários no navegador](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/e3721e16acf4d2e239296fff14a410635fac69ab/dev/back/img/gif/14-navegador.gif)|
|Fonte: Próprio autor |



| Figura 8: Autenticação de usuário|
|:-------------------:|
|![](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/e3721e16acf4d2e239296fff14a410635fac69ab/dev/back/img/gif/15-get_user_publicid.gif)|
|Fonte: Próprio autor |


| Figura 9: Autenticação de usuário |
|:-------------------:|
|![Autenticação](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/59433cd11424a42521ad35f8886a8951241da72b/dev/back/img/gif/16_autenticacao.gif)|
|Fonte: Próprio autor |

| Figura 10: Alteração de parâmetro em usuário |
|:-------------------:|
|![Alteração de parâmetros](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/59433cd11424a42521ad35f8886a8951241da72b/dev/back/img/gif/17_alteracao.gif)|
|Fonte: Próprio autor |

| Figura 11: Exclusão de usuário |
|:-------------------:|
|![Excluir usuário](https://github.com/JoseWRPereira/univesp_comp_pi3/blob/59433cd11424a42521ad35f8886a8951241da72b/dev/back/img/gif/18_exclusao.gif)|
|Fonte: Próprio autor |