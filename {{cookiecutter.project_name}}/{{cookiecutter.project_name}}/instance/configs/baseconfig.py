"""Flask related configurations with default values."""

class BaseConfig(object):
    """Default configurations for the application."""

    #############################################
    # Flask related configurations
    # uncomment/edit/modify as required or
    # include them in devel/prod specific config
    #############################################
    DEBUG = True
    TESTING = True
    # PROPAGATE_EXCEPTIONS = None
    # PRESERVE_CONTEXT_ON_EXCEPTION = None
    SECRET_KEY = 'secrit'
    SESSION_COOKIE_NAME = 'session'
    # SESSION_COOKIE_DOMAIN = None
    # SESSION_COOKIE_PATH = None
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = 86400  # 1 day in seconds
    SESSION_REFRESH_EACH_REQUEST = True
    # USE_X_SENDFILE = True
    # LOGGER_NAME = None
    # LOGGER_HANDLER_POLICY = 'always'   # other values are - debug, production, never
    # SERVER_NAME = 'domain.tld:port'
    # APPLICATION_ROOT = 'prefix'
    # MAX_CONTENT_LENGTH = 2097152  # 2mb in bytes
    # SEND_FILE_MAX_AGE_DEFAULT = 86400  # 1 day in seconds
    # TRAP_HTTP_EXCEPTIONS = True
    # TRAP_BAD_REQUEST_ERRORS = True
    # PREFERRED_URL_SCHEME = 'http'
    # JSON_AS_ASCII = False  # uncomment for utf-8 encoding
    # JSON_SORT_KEYS =True
    # JSONIFY_PRETTYPRINT_REGULAR = True
    # JSONIFY_MIMETYPE = 'application/json'
    TEMPLATES_AUTO_RELOAD = True
    # EXPLAIN_TEMPLATE_LOADING = True
