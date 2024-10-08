from setuptools import setup

setup(
    name='sauce-demo-pw-ui-tests',
    version='0.1',
    description='demo project for sauce labs ui tests building framework from '
                'scratch using playwright and python',
    author='ZS',
    author_email='sszemmouri@gmail.com',
    install_requires=[
        'behave == 1.2.6',
        'playwright == 1.45.0',
        'python-dotenv == 1.0.1',
        'pytest-base-url == 2.1.0',
        'pytest-playwright == 0.5.1',
        'robber == 1.1.5',
    ],
)
