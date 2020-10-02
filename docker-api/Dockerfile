FROM python:3.8-slim

WORKDIR /docker-api

# Copiar los archivos al contenedor
COPY . /docker-api/
COPY ./requirements.txt /docker-api/requirements.txt
#COPY ./openssl.cnf /etc/ssl/openssl.cnf

# Instalar compilador GCC
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

# Certificación necesaria para poder obtener información de MSSQL
RUN apt-get update \
    && apt-get install openssl \
    && apt-get install ca-certificates

# Instala los requirements de python al contendor
RUN pip install -r /docker-api/requirements.txt \
    && rm -rf /root/.cache/pip