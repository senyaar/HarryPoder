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
    'Django==1.7.1', #self explanatory
    'Pillow==2.3.0', #used for image uploads
    'dj_database_url', #helps manage your urls; django girls
    'djangorestframework', #api
    'markdown',       # Markdown support for the browsable API.
    'django-filter', #Filtering support
]

testing_requirements = [
    'mock==1.0.1',
    'py==1.4.26',
    'pytest==2.6.4',
    'pytest-django==2.7.0',
    'factory-boy==2.4.1',
    'tox',
]

development_requirements = [ #identical to datanav for now
    'ipdb',
    'ipython',
]


setup(name='friendmemeow',
      version='0.1.0',
      description='Michelle Senar Personal Project',
      author='Michelle Senar',
      author_email='michelle.senar@brightscope.com',
      license='All Rights Reserved',
      install_requires=requirements,
      extras_require={
            'dev': development_requirements + testing_requirements,
            'test': testing_requirements,
      },
      #scripts=['manage.py'], #my manage.py is in the same directory as this setup.py
      packages=['friendmemeow'],
      include_package_data=True,
      cmdclass={'register': DisabledCommands,
                'upload': DisabledCommands}
      )
