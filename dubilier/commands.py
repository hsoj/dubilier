"""
"""

import discord.ext.commands
from . import db


class Command(discord.ext.commands.Cog):
    """
    """

    def __init__(self, bot: discord.ext.commands.Bot, db: db.DB) -> None:
        """
        """
        super().__init__()
        self.bot = bot
        self.db = db