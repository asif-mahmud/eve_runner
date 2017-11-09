import flask_sqlalchemy
import flask_migrate

db = flask_sqlalchemy.SQLAlchemy()


def register_extensions(app):
    # SQLAlchemy specific
    db.init_app(app)
    migrate = flask_migrate.Migrate(app, db)
