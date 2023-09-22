from setuptools import setup, find_packages

setup(
    name='temper',
    version='0.1.0',
    description='A simple CLI tool to create temporary directories',
    author='Itay Shoshani',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'temper = temper.__main__:main',
        ],
    },
)