#!/bin/bash
docker-compose -f cadastro_usuarios.yml build \
--build-arg PGSQL_DB=${PGSQL_DB} \
--build-arg PGSQL_HOST=${PGSQL_HOST} \
--build-arg PGSQL_PASS=${PGSQL_PASS} \
--build-arg PGSQL_USR=${PGSQL_USR} \
--build-arg PGSQL_PORT=${PGSQL_PORT} \
--force-rm --no-cache