import os
import logging

import flask

from . import utils
from . import extensions


def create_app():
    app = flask.Flask(
        __package__.split('.')[0]
    )

    if os.environ.get('PROD', ''):
        from .configs.production import Production
        app.config.from_object(Production)
        print('[x] Production config loaded.')
    else:
        from .configs.development import Development
        app.config.from_object(Development)
        print('[x] Development config loaded.')

    # try extending loggers to use gunicorn logger
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_logger.handlers)

    # register the extensions upfront
    extensions.register_extensions(app)

    # scan for model definitions
    utils.scan_models(app)

    # register blueprints
    utils.scan_blueprints(app)

    return app
