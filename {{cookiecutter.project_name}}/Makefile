APP_NAME={{cookiecutter.project_name}}

all: initdb migrate upgrade run

run:
	python -m ${APP_NAME} -s

run_prod:
	python -m ${APP_NAME} -sp

run_tests:
	pytest

initdb:
	python -m ${APP_NAME} -r flask db init

migrate:
	python -m ${APP_NAME} -r flask db migrate

downgrade:
	python -m ${APP_NAME} -r flask db downgrade

upgrade:
	python -m ${APP_NAME} -r flask db upgrade

shell:
	python -m ${APP_NAME} -r flask shell

uwsgi:
	python -m ${APP_NAME} -u

gunicorn:
	python -m ${APP_NAME} -g

initdb_prod:
	python -m ${APP_NAME} -pr flask db init

migrate_prod:
	python -m ${APP_NAME} -pr flask db migrate

downgrade_prod:
	python -m ${APP_NAME} -pr flask db downgrade

upgrade_prod:
	python -m ${APP_NAME} -pr flask db upgrade

shell_prod:
	python -m ${APP_NAME} -pr flask shell

uwsgi_prod:
	python -m ${APP_NAME} -up

gunicorn_prod:
	python -m ${APP_NAME} -gp