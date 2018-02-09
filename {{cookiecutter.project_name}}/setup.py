import setuptools
import os

from {{cookiecutter.project_name}} import __version__

BASE_DIR = os.path.dirname(__file__)

REQ_FILE_PATH = os.path.join(BASE_DIR, 'requirements.txt')
README_FILE_PATH = os.path.join(BASE_DIR, 'README.md')

# configure application specifics
APP_NAME = '{{cookiecutter.project_name}}'
APP_VERSION = __version__
AUTHOR = '{{cookiecutter.author}}'
AUTHOR_EMAIL = '{{cookiecutter.email}}'
APP_URL = '{{cookiecutter.url}}'
APP_LICENSE = '{{cookiecutter.license}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
REQUIREMENTS = []
TESTS_REQUIREMENTS = [
    'pytest',
]
EXTRAS_REQUIRE = dict(
    gunicorn=[
        'gunicorn',
        'pastedeploy',
        'eventlet',
    ],
    uwsgi=[
        'uwsgi',
        'gevent',
    ]
)
CLASSIFIERS = [
    'Development Status :: 1-Alpha',
    'Intended Audience :: Developers',
    'Topic :: {{cookiecutter.project}}',
    'License :: GPL version 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 3.4',
]
KEY_WORDS = '{{cookiecutter.project_name}}'
PYTHON_VERSIONS = '>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4'
LONG_DESCRIPTION = ''

with open(REQ_FILE_PATH, 'r') as f:
    REQUIREMENTS.extend(f.readlines())

with open(README_FILE_PATH, 'r') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name=APP_NAME,
    version=APP_VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=APP_URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=APP_LICENSE,
    classifiers=CLASSIFIERS,
    packages=setuptools.find_packages(),
    keywords=KEY_WORDS,
    include_package_data=True,
    python_requires=PYTHON_VERSIONS,
    install_requires=REQUIREMENTS,
    tests_require=TESTS_REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
)
