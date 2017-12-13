from setuptools import setup, find_packages

setup(
    name='bank-accounts',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'Django==1.11.8',
        'psycopg2==2.7.3.2',
    ],
)
