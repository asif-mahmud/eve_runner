"""Register flask extensions here."""
import flask_migrate


def register_extensions(app):
    # SQLAlchemy Migration Facility
    migrate = flask_migrate.Migrate(app, app.data.driver)
