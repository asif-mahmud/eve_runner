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

initdb_prod:
	python -m ${APP_NAME} -rp flask db init

migrate_prod:
	python -m ${APP_NAME} -rp flask db migrate

downgrade_prod:
	python -m ${APP_NAME} -rp flask db downgrade

upgrade_prod:
	python -m ${APP_NAME} -rp flask db upgrade
