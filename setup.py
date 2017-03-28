from __future__ import print_function

from setuptools import setup, find_packages
import sys

if sys.version_info < (2, 7):
    print('You must have at least Python 2.7 for audibilize to work correctly.\n',
          file=sys.stderr)
    sys.exit(0)

if __name__ == '__main__':
    import audibilize
    setup(name='audibilize',
          version=audibilize.__version__,
          description=audibilize.__doc__,
          author=audibilize.__author__,
          license='MIT',
          packages=find_packages(),
          )
