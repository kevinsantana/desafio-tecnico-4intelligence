-- -----------------------------------------------------
-- DROP TABLES
-- -----------------------------------------------------
DROP TABLE IF EXISTS public."USUARIO";
DROP TABLE IF EXISTS public."DOMINIO_UF";
DROP TABLE IF EXISTS public."LOCALIZACAO";
DROP TABLE IF EXISTS public."LOCAL_PUBLICO";
DROP TABLE IF EXISTS public."ENDERECO";


-- -----------------------------------------------------
-- Table public."USUARIO"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public."USUARIO" (
  "id_usuario" SERIAL PRIMARY KEY,
  "nome" VARCHAR(100) NOT NULL,
  "data_nascimento" DATE NULL,
  "cpf" VARCHAR(11) NOT NULL
  );


-- -----------------------------------------------------
-- Table public."DOMINIO_UF"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public."DOMINIO_UF" (
  "id_uf" SERIAL PRIMARY KEY,
  "uf" CHAR(2) NOT NULL UNIQUE,
  "descricao" VARCHAR(30) NOT NULL UNIQUE
  );


-- -----------------------------------------------------
-- Table public."LOCALIZACAO"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public."LOCALIZACAO" (
  "id_localizacao" SERIAL PRIMARY KEY,
  "rua" VARCHAR(100) NULL,
  "numero" SMALLINT NULL,
  "cep" VARCHAR(15) NULL,
  "cidade" VARCHAR(50) NULL
  );


-- -----------------------------------------------------
-- Table public."LOCAL_PUBLICO"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public."LOCAL_PUBLICO" (
  "id_uf" INT NOT NULL,
  "id_localizacao" INT NOT NULL,
  PRIMARY KEY ("id_uf", "id_localizacao"),
  CONSTRAINT "FK_UF"
    FOREIGN KEY ("id_uf")
    REFERENCES public."DOMINIO_UF" ("id_uf")
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT "FK_LOCALIZACAO"
    FOREIGN KEY ("id_localizacao")
    REFERENCES public."LOCALIZACAO" ("id_localizacao")
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    );


-- -----------------------------------------------------
-- Table public."ENDERECO"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public."ENDERECO" (
  "id_endereco" SERIAL PRIMARY KEY,
  "id_uf" INT NOT NULL,
  "id_localizacao" INT NOT NULL,
  "id_usuario" INT NOT NULL,  
  CONSTRAINT "FK_LOCAL_PUBLICO"
    FOREIGN KEY ("id_uf" , "id_localizacao")
    REFERENCES public."LOCAL_PUBLICO" ("id_uf" , "id_localizacao")
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT "FK_USUARIO"
    FOREIGN KEY ("id_usuario")
    REFERENCES public."USUARIO" ("id_usuario")
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    );

CREATE INDEX "ID_USUARIO_INDEX" ON public."ENDERECO" ("id_usuario");


-- -----------------------------------------------------
-- INSERT "DOMINIO_UF"
-- -----------------------------------------------------
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (1, 'AC', 'ACRE');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (2, 'AL', 'ALAGOAS');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (3, 'AM', 'AMAZONAS');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (4, 'AP', 'AMAPÁ');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (5, 'BA', 'BAHIA');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (6, 'CE', 'CEARÁ');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (7, 'DF', 'DISTRITO FEDERAL');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (8, 'ES', 'ESPÍRITO SANTO');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (9, 'GO', 'GOIÁS');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (10, 'MA', 'MARANHÃO');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (11, 'MG', 'MINAS GERAIS');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (12, 'MS', 'MATO GROSSO DO SUL');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (13, 'MT', 'MATO GROSSO');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (14, 'PA', 'PARÁ');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (15, 'PB', 'PARAÍBA');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (16, 'PE', 'PERNAMBUCO');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (17, 'PI', 'PIAUÍ');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (18, 'PR', 'PARANÁ');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (19, 'RJ', 'RIO DE JANEIRO');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (20, 'RN', 'RIO GRANDE DO NORTE');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (21, 'RO', 'RONDÔNIA');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (22, 'RR', 'RORAIMA');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (23, 'RS', 'RIO GRANDE DO SUL');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (24, 'SC', 'SANTA CATARINA');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (25, 'SE', 'SERGIPE');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (26, 'SP', 'SÃO PAULO');
INSERT INTO public."DOMINIO_UF" ("id_uf", "uf", "descricao") VALUES (27, 'TO', 'TOCANTINS');
