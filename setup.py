from setuptools import setup, find_packages

setup(
    name='bank-accounts',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'Django>=1.11,<2',
        'django-allauth>=0.34,<1',
        'psycopg2>=2.7,<2.8',
    ],
)
