from setuptools import setup

setup(
    name='elden-ring-trainer',
    version='1.0.0',
    packages=['src'],
    install_requires=['numpy==1.21.2', 'configparser==5.0.1'],
    entry_points={
        'console_scripts': ['elden-ring-trainer=src.main:main'],
    }
)