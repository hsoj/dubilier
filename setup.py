"""Dubilier Python setuptools configuration.
"""


import setuptools


setuptools.setup(
    name="dubilier",
    version="0.0.1",
    install_requires=[
        "click==8.1.3",
        "discord.py==2.0.1",
        "sqlalchemy==1.4.41",
    ],
    extras_require={
        "dev": [
            "pytest==7.1.3",
            "pylint==2.15.3",
            "tox==3.26.0",
            "mypy==0.982",
            "yapf==0.32.0",
            "pre-commit==2.20.0",
            "coverage==6.5.0",
        ]
    },
    entry_points={
        "console_scripts": {
            "dubilier = dubilier.__main__:main"
        }
    }
)