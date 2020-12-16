# Instalação e Execução

A execução da aplicação é dividida em duas partes: `build` das imagens consumidas pelos containers e a execução dos containers. Para o [build](./build.sh) das imagens é necessário executar o seguinte comando:

```bash
bash build.sh
```

Com as imagens _buildadas_ é possível executar os containers, através do comando:

```bash
bash run.sh
```

Com a aplicação no ar, basta acessar o [ReDoc](http://localhost:7000/v1/docs) para saber como utilizar cada um dos *endpoints* e para utilizar os *endpoints* acesse o [Swagger](http://localhost:7000/v1/swagger).

Com todo o ambiente rodando, antes mesmo de instalar e rodar a aplicação, é preciso executar a query de criação no banco de dados. Entre no PGAdmin configure o acesso ao banco de dados e execute a query do arquivo [`create.sql`]().
