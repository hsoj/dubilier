"""Dubilier Python setuptools configuration.
"""


import setuptools


setuptools.setup(
    name="dubilier",
    version="0.0.1",
    install_requires=[
        "click",
        "discord.py",
        "sqlalchemy",
    ],
    extras_require={
        "dev": [
            "pytest", "pylint", "tox", "mypy", "yapf", "pre-commit",
            "coverage",
        ]
    },
    entry_points={
        "console_scripts": {
            "dubilier = dubilier.__main__:main"
        }
    }
)