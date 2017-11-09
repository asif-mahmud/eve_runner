"""{{cookiecutter.project}} package documentation."""


__version__ = '{{cookiecutter.project_version}}'


def main(env, **kw):
    """Entry point for `gunicorn` server."""
    import {{cookiecutter.project_name}}.instance.app as app

    application = app.create_app()

    return application
