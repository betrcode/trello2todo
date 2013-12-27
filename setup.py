from distutils.core import setup

setup(
    name='Trello2ToDo',
    version='0.1.0',
    author='Max Wenzin',
    author_email='max.wenzin@gmail.com',
    packages=['trello2todo', 'trello2todo.test'],
    url='http://pypi.python.org/pypi/Trello2ToDo/',
    license='LICENSE.txt',
    description='Can migrate your Trello data to Projectplace ToDo.',
    long_description=open('README.txt').read(),
    install_requires=[],
)
