#
# Copyright (c) 2022, 2023 by Delphix. All rights reserved.
#
.PHONY: --check_python --check_env_exists run tests --create_virtual_env --install_dependencies env clean_build clean_env clean build docker-image docker-run docker-stop docker-rm docker-start docker-save export-requirements

ROOT_DIR := $(shell pwd)
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
POETRY := $(VENV)/bin/poetry
UVICORN := $(VENV)/bin/uvicorn
ALEMBIC := $(VENV)/bin/alembic
red := $(shell tput setaf 1)
reset := $(shell tput sgr0)
SITE_PACKAGE_PATH := $(VENV)/lib/python3.9/site-packages
REPO := https://artifactory.delphix.com/artifactory/api/pypi/delphix-local
DOCKER_CONTAINER_NAME := mongo-hsc-load-container
DOCKER_IMAGE_NAME := delphix-mongo-load-service-app
DOCKER_BUILD_NAME := mongo-load-service.tar
USER := $(shell whoami)
LOG_FOLDER := /opt/delphix/logs/
VERSION := latest

define check_python_exists
	@if ! command -v python3.9 -V >/dev/null 2>&1; then \
		echo "Python 3.9 is NOT present on the system, Please install it"; \
		exit 1; \
	fi
endef

--check_python:
	@# Help: Checks existence of python virtual environment
	$(call check_python_exists)

--check_env_exists: --check_python
	@[ -f $(PYTHON) ] && echo $(PYTHON) exists || (echo $(PYTHON) does NOT exist, use \"make env\" to create a virtual env; exit 1)


$(LOG_FOLDER):
	-sudo mkdir -p $(LOG_FOLDER)
	-sudo chown -R $(USER) $(LOG_FOLDER)

run: --check_env_exists --export_lang $(LOG_FOLDER)
	@# Help: Runs the Fast API server on port 8080 using uvicorn
	-@$(ALEMBIC) upgrade head
	-@echo 'Running the app...'
	-$(UVICORN) src.main:app --host 0.0.0.0 --port 8080 --reload

tests:
	@# Help: Runs the unit tests inside tests folder and create a report
	$(PYTHON) -m pytest tests -s -v

--create_virtual_env: --check_python
	@# Help: Creates a virtual environment
	-@echo 'Creating Virtual environment'
	@python3.9 -m venv $(VENV) || echo 'Python env already exists'

--install_dependencies:
	@# Help: Installs the dev dependencies using poetry
	-@echo 'Installing Dependencies...'
	@$(PYTHON) -m pip install --upgrade pip
	@$(PIP) install rpds-py==0.7.1
	@$(PIP) install poetry==1.5.1
	@$(POETRY) config virtualenvs.in-project true
	@$(POETRY) config --list
	@$(POETRY) install --no-root

export-requirements:
	@# Help: Exports the python dependencies from poetry to requirements.txt
	@$(POETRY) export -o requirements.txt


env: --create_virtual_env --install_dependencies
	@# Help: Creates a virtual environment with python3.9 if not already present and activates it
	-@echo "Attaching pre commit";
	-@$(VENV)/bin/pre-commit install

clean_env:
	@# Help: Clean the virtual env that was created
	-@rm -rf $(VENV)

clean_build:
	@# Help: Cleans the build files
	-@rm -rf build/
	-@rm -rf dist/

clean: clean_build
	@# Help: Cleans the pycache, coverage and build files
	-@rm -rf __pycache__
	-@rm -f .coverage
	-@rm -rf tests/.pytest_cache
	-@rm -rf tests/CodeCoverage
	-@rm -rf tests/Report.html
	-@rm -rf .pytest_cache/

docker-image:
	@# Help: Creates the docker image
	-@docker build -t $(DOCKER_IMAGE_NAME):$(VERSION) .

docker-run: docker-rm docker-image
	@# Help: Runs the docker container using the created image
	-@docker run -d -p 8081:8080 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME):$(VERSION)
	-@docker ps
	-@echo "The $(DOCKER_CONTAINER_NAME) swagger UI can be accessed at http://0.0.0.0:8081"

docker-start:
	@# Help: Starts the docker container
	-@docker start $(DOCKER_CONTAINER_NAME)
	-@echo "Started the container"
	-@echo "The $(DOCKER_CONTAINER_NAME) swagger UI can be accessed at http://0.0.0.0:8081"

docker-stop:
	@# Help: Stops the docker container
	-@docker stop $(DOCKER_CONTAINER_NAME)
	-@echo "Stopped the container"

docker-rm: docker-stop
	@# Help: Removes the docker container
	-@docker rm $(DOCKER_CONTAINER_NAME)
	-@docker image rm $(DOCKER_IMAGE_NAME):$(VERSION)
	-@echo "Removed the container and image"

docker-save: clean_build docker-image
	@# Help: Save the docker images to build folder
	-@mkdir build
	-@docker save $(DOCKER_IMAGE_NAME):$(VERSION) -o build/$(DOCKER_BUILD_NAME)

--export_lang:
	LC_ALL=en_AU.UTF-8
	PYTHONPATH=$(ROOT_DIR)
	@export LC_ALL
	@export PYTHONPATH
	-@echo 'All env variables exported'


# A hidden target
.hidden:
help:
	@printf "%-20s %s\n" "Target" "Description"
	@printf "%-20s %s\n" "------" "-----------"
	@make -pqR : 2>/dev/null \
        | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' \
        | sort \
        | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' \
        | xargs -I _ sh -c 'printf "%-20s " _; make _ -nB | (grep -i "^# Help:" || echo "") | tail -1 | sed "s/^# Help: //g"'