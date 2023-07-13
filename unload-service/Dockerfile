#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

FROM python:3.9-slim as build

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.5.1

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"  \
    && poetry install --without dev --no-root --no-ansi --no-interaction \
    && poetry export --without dev -o requirements.txt \
    && pip uninstall --yes poetry


FROM python:3.9-slim as final

WORKDIR /app

COPY --from=build /app/requirements.txt .

# env variables for docker container to recognize the app
ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1 \
    MODULE_NAME=src.main \
    PORT=8080 \
    LOG_LEVEL=debug

# Create a non-root user
# Upgrade the package index and install security upgrades
# Install python dependencies
# Install MongoDB tools and mongosh utility
# Clean up
# Create folder for log and assign permissions
RUN set -ex &&  \
    addgroup --system --gid 1001 delphix &&  \
    adduser --system --uid 1001 --gid 1001 --no-create-home delphix && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y wget sqlite3 && \
    pip install --no-cache-dir -r requirements.txt && \
    wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-rhel80-x86_64-100.7.2.tgz && \
    wget https://downloads.mongodb.com/compass/mongosh-1.10.0-linux-x64.tgz && \
    tar -zxvf mongodb-database-tools-rhel80-x86_64-100.7.2.tgz -C /app && \
    mv /app/mongodb-database-tools-rhel80-x86_64-100.7.2 /app/mongodb-database-tools && \
    tar -zxvf mongosh-1.10.0-linux-x64.tgz -C /app && \
    mv /app/mongosh-1.10.0-linux-x64 /app/mongosh && \
    find /app/mongodb-database-tools/bin ! -name 'mongoexport' -type f -exec rm -f {} \; && \
    mv /app/mongosh/bin/mongosh /app/mongodb-database-tools/bin && \
    rm -rf mongodb-database-tools-*.tgz mongosh-1.10.0-*.tgz /app/mongosh && \
    apt-get remove -y wget && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /opt/delphix/logs/ &&  \
    chown -R delphix:delphix /opt/delphix/logs/ && \
    chown -R delphix:delphix /app

COPY ./container_conf/app_files/* ./alembic.ini /app/
COPY ./container_conf/root_files/* /
COPY ./migrations /app/migrations
COPY ./src /app/src

# Set the user to run the application
USER delphix

ENTRYPOINT ["../start.sh"]