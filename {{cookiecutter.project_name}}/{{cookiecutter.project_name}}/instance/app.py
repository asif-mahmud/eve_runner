"""Implementation of app factory."""

import os
import logging

import eve
import eve_sqlalchemy as es

from . import utils
from . import extensions
from . import db


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
        validator=db.UUIDValidator,
        json_encoder=db.UUIDEncoder,
        data=es.SQL,
    )

    app.config.update(app_settings)

    # register the extensions upfront
    extensions.register_extensions(app)

    # scan for model definitions
    utils.scan_models(app)
    utils.register_resources(app)

    # register blueprints
    utils.scan_blueprints(app)

    return app
