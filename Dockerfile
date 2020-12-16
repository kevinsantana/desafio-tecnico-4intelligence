FROM python:3.8-alpine3.12

# ENV VARS

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

EXPOSE 7000
CMD ["gunicorn", "--bind=0.0.0.0:7000", "--workers=3", "--worker-class=uvicorn.workers.UvicornWorker", "--timeout=174000", "cadastro_usuarios:app"]
