FROM python:3.8-alpine3.12

# ENV VARS
ARG PGSQL_DB
ARG PGSQL_HOST
ARG PGSQL_PASS
ARG PGSQL_PORT
ARG PGSQL_USR


ENV PGSQL_DB="$PGSQL_DB"
ENV PGSQL_HOST="$PGSQL_HOST"
ENV PGSQL_PASS="$PGSQL_PASS"
ENV PGSQL_PORT="$PGSQL_PORT"
ENV PGSQL_USR="$PGSQL_USR"

# DEPENDENCIES
RUN apk add build-base \
    && apk add poppler-utils --no-cache \
    && apk add postgresql-dev --no-cache

# INSTALL APPLICATION
COPY ./cadastro_usuarios /deploy/cadastro_usuarios
COPY ./docs /deploy/docs
COPY setup.py /deploy
COPY README.md /deploy
COPY /tests /deploy/tests

WORKDIR /deploy

RUN pip install -e .

EXPOSE 3000
CMD ["gunicorn", "--bind=0.0.0.0:3000", "--workers=3", "--worker-class=uvicorn.workers.UvicornWorker", "--timeout=174000", "cadastro_usuarios:app"]
