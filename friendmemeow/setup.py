import platform
from setuptools import setup, find_packages
from distutils.core import Command

class DisabledCommands(Command): #not sure if needed, but in the datanav one
  user_options = []

  def initialize_options(self):
    raise Exception('This command is disabled')

  def finalize_options(self):
    raise Exception('This command is disabled')

requirements = [
    'Django==1.7.1',
    'Pillow==2.3.0',
    'whitenoise==1.0.4',
    'wsgiref==0.1.2',
]

testing_requirements = [
    'Django==1.7.1',
    'Pillow==2.3.0',
    'mock==1.0.1',
    'py==1.4.26',
    'pytest==2.6.4',
    'pytest-django==2.7.0',
    'whitenoise==1.0.4',
    'wsgiref==0.1.2',
]

development_requirements = [ #identical to datanav for now
    'ipdb',
    'ipython',
]

production_requirements = [ #same as above
    'gunicorn==19.1.1',
]

if platform.python_implementation() == "PyPy":
  requirements.append("psycopg2cffi==2.5")
else:
  requirements.append('psycopg2==2.5.2')

setup(name='friendmemeow',
      version='0.1.0',
      description='Michelle Senar Personal Project',
      author='Michelle Senar',
      author_email='michelle.senar@brightscope.com',
      license='All Rights Reserved',
      install_requires=requirements,
      extras_require={
            'dev': development_requirements + testing_requirements,
            'prod': production_requirements,
            'test': testing_requirements,
      },
      scripts=['manage.py'], #my manage.py is in the same directory as this setup.py
      package_dir={'': 'finder'}, #finder is the package here
      packages=find_packages(where='finder', exclude=('tests*',)),
      include_package_data=True,
      cmdclass={'register': DisabledCommands,
                'upload': DisabledCommands}
      )
