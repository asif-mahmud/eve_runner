"""Utilities to properly and fully load the application."""

import os
import importlib
import setuptools


def scan_models(app):
    """Scan the package for model definitions."""
    for dirpath, dirnames, filenames in os.walk(app.root_path):
        head, tail = os.path.split(dirpath)
        if tail in app.config['MODEL_DIRS']:
            # there should be models
            for filename in filenames:
                if filename.endswith('.py') and \
                        filename not in app.config['MODEL_EXCLUDE_FILES']:
                    # lets import the module
                    filename_no_ext, _ = os.path.splitext(
                        os.path.join(
                            dirpath, filename
                        )
                    )
                    # remove app.root_path and / characters
                    filename_no_ext = filename_no_ext.replace(
                        app.root_path, __package__.split('.')[0]
                    )
                    module_path = filename_no_ext.replace(os.sep, '.')
                    importlib.import_module(module_path)


def scan_blueprints(app):
    """Scan and register all blueprints.

    Blueprints may be implemented by factory model. Any package under
    `blueprints` package will be considered as a blueprint and will be attempted
    to register. To allow registering, make a function named `create_blueprint`
    which must return `(blueprint, prefix)` pair where `blueprint` is the 
    `flask.Blueprint` instance and `prefix` is the prefix for loading the 
    blueprint at. Another way will be setting two package variables - `__blueprint__`
    for `flask.Blueprint` instance and `__prefix__` for url prefix.
    """
    blueprints_path = os.path.join(
        app.root_path,
        'blueprints'
    )
    packages = setuptools.find_packages(blueprints_path)
    for pac in packages:
        factory_module = importlib.import_module(
            '.'.join([
                __package__.split('.')[0],
                'blueprints',
                pac
            ])
        )
        if factory_module:
            if hasattr(factory_module, 'create_blueprint'):
                blueprint, prefix = getattr(
                    factory_module, 'create_blueprint'
                )()
                app.register_blueprint(
                    blueprint, url_prefix=prefix
                )
            elif hasattr(factory_module, '__blueprint__') and \
                    hasattr(factory_module, '__prefix__'):
                app.register_blueprint(
                    getattr(factory_module, '__blueprint__'),
                    url_prefix=getattr(factory_module, '__prefix__')
                )
