
from setuptools import setup, find_packages

setup(
        name='terminology-tools',

        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # https://packaging.python.org/en/latest/single_source_version.html
        version='0.1',

        description='Terminology Tools',
        long_description='Better tools for use with Terminology',

        # The project's main homepage.
        url='https://github.com/pjz/terminology-tools',

        # Author details
        author='Paul Jimenez',
        author_email='pj@place.org',

        # Choose your license
        license='GPLv3',

        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Programming Language :: Python :: 3',
        ],
        keywords = 'terminology',
        packages = find_packages(),
        install_requires = [ 'click', 'blessings' ]
)

