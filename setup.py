from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    version='0.0.1',
    name='organizer',
    packages=find_packages(),
    entry_points={
        'console_scripts': [ 
            'organizer=main:main', 
        ]
    },
    install_requires=install_requires,
)
