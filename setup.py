
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MyProject',
    version='0.1.0',
    description='Sample package for MyProject',
    long_description=readme,
    author='Saurav Adhikari',
    author_email='ad.saurav@gmail.com',
    url='https://github.com/ad-saurav/MyProject',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)