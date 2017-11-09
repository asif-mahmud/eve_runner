APP_NAME={{cookiecutter.project_name}}
APP_PATH=${APP_NAME}.application

all: setup initdb run

run:
	gunicorn --paste gunicorn/dev.ini

run_prod:
	PROD=1 gunicorn --paste gunicorn/prod.ini

run_tests:
	pytest

setup:
	pip install -e . --upgrade

initdb:
	FLASK_APP=${APP_PATH} flask db init

migrate:
	FLASK_APP=${APP_PATH} flask db migrate

downgrade:
	FLASK_APP=${APP_PATH} flask db downgrade

upgrade:
	FLASK_APP=${APP_PATH} flask db upgrade
