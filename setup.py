from setuptools import setup
# from setuptools import find_packages
from setuptools.command.test import test as testcommand
import sys
import re
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        print('VERSION: ', version_match.group(1))
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


class Tox(testcommand):
    def finalize_options(self):
        testcommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='cloudify-release-toollll',
    version='3.3m4',
    url='https://github.com/cloudify-cosmo/cloudify-build-system',
    author='Gigaspaces',
    author_email='cosmo-admin@gigaspaces.com',
    license='LICENSE',
    platforms='All',
    description='Cloudify Release Tool',
    long_description=read('README.rst'),
    packages=['crt'],
    entry_points={
        'console_scripts': [
            'crt = crt.crt:main',
        ]
    },
    install_requires=[
        'click==4.0',
        'pyyaml==3.10',
        'gitpython==0.3.6',
        'repex==0.1.2',
        'python-vagrant==0.5.8',
        'fabric==1.10.1',
        'gitpython==0.3.6',
        'boto==2.36.0',
        'jira==0.47',
    ],
    tests_require=['nose', 'tox'],
    cmdclass={'test': Tox},
)
