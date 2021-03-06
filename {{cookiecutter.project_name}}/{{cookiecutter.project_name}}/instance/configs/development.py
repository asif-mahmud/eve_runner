"""Development configuration."""

from .baseconfig import APP_CONFIG

APP_CONFIG.update(dict(
    #########################################
    # Flask related configurations
    #########################################

    ##############################################
    # Flask-SQLAlchemy related configs
    # override to have deployment specific config
    ##############################################
    SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite',
    # SQLALCHEMY_BINDS = dict(),
    SQLALCHEMY_ECHO=True,
    # SQLALCHEMY_RECORD_QUERIES = True,
    # SQLALCHEMY_NATIVE_UNICODE = False,
    # SQLALCHEMY_POOL_SIZE = 5,
    # SQLALCHEMY_POOL_TIMEOUT = 10,   # in seconds
    # SQLALCHEMY_POOL_RECYCLE = 10,   # in seconds
    # SQLALCHEMY_MAX_OVERFLOW = 10,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    ##########################################
    # SQLAlchemy Models scanner configurations
    ##########################################
    MODEL_DIRS=[
        'models',   # any directory named models will be looked into
    ],
    MODEL_EXCLUDE_FILES=[
        '__init__.py',  # __init__.py should not have any model definition
    ],
))
