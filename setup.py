
from setuptools import setup, find_packages
from tvControlCLI.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='tvcli',
    version=VERSION,
    description='MyApp Does Amazing Things!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Fabian Escarate',
    author_email='john.doe@example.com',
    url='https://github.com/johndoe/myapp/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'tvcli': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        tvcli = tvcli.main:main
    """,
)
