Flask Runner
=========================

This is a [Flask](http://flask.pocoo.org/) project template for large application developers who intend to modularise their application by utilizing `flask.Blueprint`. 

This is a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template, so to generate a project using this template use `cookiecutter`.

### Features

* Minimal setup
* Factory based application structure
* Blueprints are auto registered (yes automatically registered! see below)
* Separate configuration for development and production application
* Uses [Gunicorn](http://gunicorn.org/) for both development and production server
* Uses [Eventlet](http://eventlet.net/) worker to allow implementing asynchronous apps(i.e SocketIO by [Flask-SocketIO](https://flask-socketio.readthedocs.io))
* Only assumption made during making the template is that the developer may want to use [SQLAlchemy](https://www.sqlalchemy.org/), so [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) are preconfigured. The developer only has to change SQLAlchemy related configurations. This can be changed or removed to use other options very easily.
* Easy `Makefile` syntax for running, testing, migrating application and it's databases.
* Auto loads SQLAlchemy models at the application startup. So no need to import all model moduls by hand.