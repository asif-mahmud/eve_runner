"""Run the application server from command line.

This module allows the developer or deployer to run the
application with different configs or commands as needed
from the command line.

This also is a replacement for `Makefile` based setup
"""
import os
import abc
import shlex
import argparse
import subprocess


def setup_args():
    """Argument parser setup."""
    parser = argparse.ArgumentParser(
        prog=__package__.split('.')[0],
        usage='Run the app server through different and suitable commands.',
    )
    parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter

    parser.add_argument(
        '--run', '-r', nargs='+', help='Start a process to execute the RUN command.',
    )
    parser.add_argument(
        '--serve', '-s', default=False, action='store_true',
        help='Spawn the application server.'
    )
    parser.add_argument(
        '--gunicorn', '-g', default=False, action='store_true',
        help='Run gunicorn server.'
    )
    parser.add_argument(
        '--uwsgi', '-u', default=False, action='store_true',
        help='Run uWSGI server.'
    )
    parser.add_argument(
        '--prod', '-p', default=False, action='store_true',
        help='Setup production environment for running the RUN command.'
    )

    return parser, vars(parser.parse_args())


class BaseProcessSpawner(abc.ABC):

    def __init__(self, args):
        self._args = args

    @abc.abstractmethod
    def set_env(self):
        """Method to set environmental variables.

        Returns:
            env(dict): Copied and edited environ dictionary
        """
        pass

    def spawn_process(self):
        """Spawn the process."""
        try:
            env = self.set_env()
            process = subprocess.Popen(self._args['run'], env=env)
            process.communicate()
        except KeyboardInterrupt:
            print('Exiting ...')
        except Exception as err:
            print(err)


class DevProcessSpawner(BaseProcessSpawner):

    def set_env(self):
        rv = os.environ.copy()
        rv['FLASK_APP'] = '{}.application'.format(
            __package__.split('.')[0]
        )
        rv['FLASK_DEBUG'] = '1'
        return rv


class ProdProcessSpawner(BaseProcessSpawner):

    def set_env(self):
        rv = os.environ.copy()
        rv['FLASK_APP'] = '{}.application'.format(
            __package__.split('.')[0]
        )
        rv['PROD'] = '1'
        return rv


if __name__ == '__main__':
    parser, args = setup_args()
    if args['serve']:
        args['run'] = shlex.split('flask run --port=8000')
    if args['gunicorn']:
        ini_dir = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'gunicorn'
            )
        )
        args['run'] = shlex.split('gunicorn --paste {}'.format(
            os.path.join(ini_dir, 'prod.ini')
        )) if args['prod'] else shlex.split('gunicorn --paste {}'.format(
            os.path.join(ini_dir, 'dev.ini')
        ))
    if args['uwsgi']:
        ini_dir = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'uwsgi'
            )
        )
        args['run'] = shlex.split('uwsgi --ini {}'.format(
            os.path.join(ini_dir, 'prod.ini')
        )) if args['prod'] else shlex.split('uwsgi --ini {}'.format(
            os.path.join(ini_dir, 'dev.ini')
        ))
    try:
        spawner = ProdProcessSpawner(
            args
        ) if args['prod'] else DevProcessSpawner(args)
        spawner.spawn_process()
    except Exception:
        parser.print_help()
