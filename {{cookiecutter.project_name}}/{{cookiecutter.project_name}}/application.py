"""Application instance for {{cookiecutter.project}}.

Use this module for rnning by `flask run` command or 
importing the application instance to use with other applications.

When running this application by `gunicorn` this instance is not 
used at all. Gunicorn will use the `main` function to instantiate 
the app.

This is also used for database migrations by `Flask-Migrate`.
"""
from . import main

application = main({})
