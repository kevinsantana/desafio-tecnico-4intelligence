-- -----------------------------------------------------
-- DROP TABLES
-- -----------------------------------------------------
DROP TABLE IF EXISTS public.USUARIO CASCADE;
DROP TABLE IF EXISTS public.DOMINIO_UF CASCADE;
DROP TABLE IF EXISTS public.LOCALIZACAO CASCADE;
DROP TABLE IF EXISTS public.LOCAL_PUBLICO CASCADE;
DROP TABLE IF EXISTS public.ENDERECO CASCADE;


-- -----------------------------------------------------
-- Table public.USUARIO
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.USUARIO (
  ID_USUARIO SERIAL PRIMARY KEY,
  NOME VARCHAR(100) NOT NULL,  
  CPF VARCHAR(11) NOT NULL UNIQUE,
  DATA_NASCIMENTO TIMESTAMP NULL
  );


-- -----------------------------------------------------
-- Table public.DOMINIO_UF
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.DOMINIO_UF (
  ID_UF SERIAL PRIMARY KEY,
  UF CHAR(2) NOT NULL UNIQUE,
  DESCRICAO VARCHAR(30) NOT NULL UNIQUE
  );


-- -----------------------------------------------------
-- Table public.LOCALIZACAO
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.LOCALIZACAO (
  ID_LOCALIZACAO SERIAL PRIMARY KEY,
  RUA VARCHAR(100) NULL,
  NUMERO SMALLINT NULL,
  CEP VARCHAR(15) NULL,
  CIDADE VARCHAR(50) NULL
  );


-- -----------------------------------------------------
-- Table public.LOCAL_PUBLICO
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.LOCAL_PUBLICO (
  ID_UF INT NOT NULL,
  ID_LOCALIZACAO INT NOT NULL,
  PRIMARY KEY (ID_UF, ID_LOCALIZACAO),
  CONSTRAINT FK_UF
    FOREIGN KEY (ID_UF)
    REFERENCES public.DOMINIO_UF (ID_UF)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT FK_LOCALIZACAO
    FOREIGN KEY (ID_LOCALIZACAO)
    REFERENCES public.LOCALIZACAO (ID_LOCALIZACAO)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    );


-- -----------------------------------------------------
-- Table public.ENDERECO
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.ENDERECO (
  ID_ENDERECO SERIAL PRIMARY KEY,
  ID_UF INT NOT NULL,
  ID_LOCALIZACAO INT NOT NULL,
  ID_USUARIO INT NOT NULL,  
  CONSTRAINT FK_LOCAL_PUBLICO
    FOREIGN KEY (ID_UF , ID_LOCALIZACAO)
    REFERENCES public.LOCAL_PUBLICO (ID_UF , ID_LOCALIZACAO)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT FK_USUARIO
    FOREIGN KEY (ID_USUARIO)
    REFERENCES public.USUARIO (ID_USUARIO)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    );

CREATE INDEX ID_USUARIO_INDEX ON public.ENDERECO (ID_USUARIO);


-- -----------------------------------------------------
-- INSERT DOMINIO_UF
-- -----------------------------------------------------
INSERT INTO public.DOMINIO_UF (UF, DESCRICAO)
VALUES 
    ('AC', 'ACRE'),
    ('AL', 'ALAGOAS'),
    ('AM', 'AMAZONAS'),
    ('AP', 'AMAPÁ'),
    ('BA', 'BAHIA'),
    ('CE', 'CEARÁ'),
    ('DF', 'DISTRITO FEDERAL'),
    ('ES', 'ESPÍRITO SANTO'),
    ('GO', 'GOIÁS'),
    ('MA', 'MARANHÃO'),
    ('MG', 'MINAS GERAIS'),
    ('MS', 'MATO GROSSO DO SUL'),
    ('MT', 'MATO GROSSO'),
    ('PA', 'PARÁ'),
    ('PB', 'PARAÍBA'),
    ('PE', 'PERNAMBUCO'),
    ('PI', 'PIAUÍ'),
    ('PR', 'PARANÁ'),
    ('RJ', 'RIO DE JANEIRO'),
    ('RN', 'RIO GRANDE DO NORTE'),
    ('RO', 'RONDÔNIA'),
    ('RR', 'RORAIMA'),
    ('RS', 'RIO GRANDE DO SUL'),
    ('SC', 'SANTA CATARINA'),
    ('SE', 'SERGIPE'),
    ('SP', 'SÃO PAULO'),
    ('TO', 'TOCANTINS');
