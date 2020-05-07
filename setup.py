from setuptools import setup

setup(
    name="randomizer",
    version='1.0',
    py_modules=['randomizer'],
    install_requires=[
        'Click',
	'prettytable',
	'pyfiglet'

    ],
    entry_points='''
        [console_scripts]
        randomizer=randomizer:cli
    ''',
)
