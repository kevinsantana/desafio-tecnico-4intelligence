# Prerequisites

Caso o desenvolvedor opte por executar a solução de forma não _dockerizada_, sugere-se a criação de um ambiente virtual para instalação das dependências da aplicação, como por exemplo o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

Para instalar as dependências do projeto, execute:

```bash
pip3 install -e .
```

Além disso, é preciso inicializar os softwares de dependência, são eles:

* [`PostgreSQL`](https://www.postgresql.org): Banco de dados relacional para manter um usuário.
* [`PGAdmin`](https://www.pgadmin.org): Permite a comunicação com o banco de dados `PostgreSQL` através de uma interface gráfica, exposta por uma URL.

No cenário em que o desevolvedor opte por executar a aplicação de forma _dockerizada_(recomendada) é preciso possuir o [docker](https://docs.docker.com/) e o [docker-compose](https://docs.docker.com/compose/) instalados.

As variáveis de ambiente listadas abaixo devem estar exportadas no terminal para serem consumidas através do `docker-compose`, conforme instruções do passo seguinte `Instalação e Execução`. Enquanto o valor das variáveis mudam conforme a necessidade de execução, os nomes devem permanecer os mesmos, são eles:

* `PGADMIN_DEFAULT_EMAIL`: _email_ utilizado no momento de criação do container `PGAdim` permitindo o login;
* `PGADMIN_DEFAULT_PASSWORD`: _password_ utilizado no momento de execução do container `PGAdim` permitindo o login;

* `POSTGRES_DB`: Nome do banco de dados utilizado para criação do banco de dados, consumido pelo container do banco de dados;
* `POSTGRES_USER`: Usuário do banco de dados utilizado para criação do banco de dados, consumido pelo container do banco de dados;
* `POSTGRES_PASSWORD`: Senha do banco de dados utilizado para criação do banco de dados, consumido pelo container do banco de dados.
