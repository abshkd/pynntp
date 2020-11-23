from setuptools import setup


setup(
    name='pynntp',
    version='1.0.1',
    description='NNTP Library (including compressed headers)',
    author='Byron Platt',
    author_email='byron.platt@gmail.com',
    license='GPL3',
    url='https://github.com/greenbender/pynntp',
    packages=['nntp'],
    install_requires=['dateutils'],
    python_requires='>=2.7',
)
