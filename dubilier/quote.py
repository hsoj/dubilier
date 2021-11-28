"""
"""


import discord.ext.commands
from . import (
    db,
    commands,
)


class Command(db.Mixin,
              commands.Command):
    """
    """
    SCHEMA = """
    CREATE TABLE IF NOT EXISTS quotes (
        id integer PRIMARY KEY,
        quote text
    );
    """