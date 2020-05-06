from setuptools import setup

setup(
    name="randomizer",
    version='0.1',
    py_modules=['randomizer'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        randomizer=randomizer:cli
    ''',
)
