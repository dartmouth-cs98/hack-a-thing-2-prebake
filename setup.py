from setuptools import setup

setup(
    name='lassh',
    author='Steven Chun',
    author_email='schunchicago@gmail.com',
    url='https://github.com/dartmouth-cs98/hack-a-thing-2-prebake',
    version='0.1.0',
    packages=['lassh'],
    install_requires=[
        'Click',
        'sshconf',
        'setuptools',
        'clint',
        'pathlib'
    ],
    entry_points={
        'console_scripts': [
            'lassh=lassh.__main__:main'         
        ]
    },
)
