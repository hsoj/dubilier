"""Dubilier Python setuptools configuration.
"""

import setuptools


setuptools.setup(
    name="dubilier",
    version="0.0.1",
    install_requires=[
        "click",
        "discord.py",
    ],
    extra_requires={
        "dev": [
            "pytest", "pylint", "tox", "mypy", "yapf",
        ]
    }
)