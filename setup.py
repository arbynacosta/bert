import os
import subprocess
from subprocess import CalledProcessError

from setuptools import find_packages
from setuptools import setup

__version__ = '1.0.3'
__title__ = 'bert'


version = __version__

try:
    cmd = 'git rev-parse HEAD'.split(' ')
    version += subprocess.check_output(cmd).decode('utf-8')

except CalledProcessError:
    pass


def get_dependencies():
    # Get the requirements.txt
    root_dir = os.path.dirname(os.path.realpath(__file__))
    requirements_file = root_dir + '/requirements.txt'

    # Build install requirements
    install_requires = []
    if os.path.isfile(requirements_file):
        with open(requirements_file) as opened_file:
            install_requires = opened_file.read().splitlines()

    return install_requires


setup(
    name=__title__,
    version=version,
    packages=find_packages(exclude=[
        '*_test*'
    ]),
    install_requires=get_dependencies(),
)
