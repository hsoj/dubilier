"""Module that provides an object which other commands added to the bot
can leverage generic operations.
"""


import discord.ext.commands


class Base(discord.ext.commands.Cog):
    """Base object which other command objects can inherit to ensure
    that all of the required properties and methods are included
    within the command object.
    """

    def __init__(self) -> None:
        pass
