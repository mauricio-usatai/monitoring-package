from setuptools import setup, find_packages

setup(
	name = 'monitoring',
	version = '1.0.0',
  packages = find_packages(),
  install_requires = [
    'boto3==1.25.4',
    'botocore==1.28.4',
    'certifi==2022.9.24',
    'charset-normalizer==2.1.1',
    'click==8.1.3',
    'Flask==2.2.2',
    'idna==3.4',
    'importlib-metadata==5.0.0',
    'itsdangerous==2.1.2',
    'Jinja2==3.1.2',
    'jmespath==1.0.1',
    'MarkupSafe==2.1.1',
    'python-dateutil==2.8.2',
    'requests==2.28.1',
    's3transfer==0.6.0',
    'six==1.16.0',
    'typing_extensions==4.4.0',
    'urllib3==1.26.12',
    'Werkzeug==2.2.2',
    'zipp==3.10.0',
  ],
)