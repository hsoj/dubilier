"""
"""


import discord.ext.commands
from . import (
    db,
    commands,
)

class Bot(discord.ext.commands.Bot):
    """
    """
    DEFAULT_PREFIX = "?"

    def __init__(self, **kwargs: dict) -> None:
        super().__init__(
            command_prefix=kwargs.get("prefix", self.DEFAULT_PREFIX),
        )
        self.db = db.DB(path=kwargs.get("db_path", None))
        self.token = kwargs.get("token", None)

    def add_cmd(self, command: commands.Command) -> None:
        """
        """
        cmd = command(bot=self, db=self.db)
        self.add_cog(cmd)

    def run(self) -> None:
        """
        """
        super().run(self.token)