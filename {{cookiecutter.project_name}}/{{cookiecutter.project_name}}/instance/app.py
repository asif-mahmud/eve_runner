"""Implementation of app factory."""

import os
import logging

import eve
import eve_sqlalchemy as es
import eve_sqlalchemy.validation as es_v

from . import utils
from . import extensions


def create_app():
    app_settings = {}
    if os.environ.get('PROD', ''):
        from .configs.production import APP_CONFIG
        app_settings = APP_CONFIG
        print('[x] Production config loaded.')
    else:
        from .configs.development import APP_CONFIG
        app_settings = APP_CONFIG
        print('[x] Development config loaded.')

    app = eve.Eve(
        __package__.split('.')[0],
        settings=app_settings,
        validator=es_v.ValidatorSQL,
        data=es.SQL,
    )

    app.config.update(app_settings)

    # try extending loggers to use gunicorn logger
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_logger.handlers)

    # register the extensions upfront
    extensions.register_extensions(app)

    # scan for model definitions
    utils.scan_models(app)
    utils.register_resources(app)

    # register blueprints
    utils.scan_blueprints(app)

    return app
