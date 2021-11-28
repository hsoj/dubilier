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
        self.db = db.Connection(path=kwargs.get("db_path", ":memory:"))
        self.token = kwargs.get("token", None)

    def add_cmd(self, command: commands.Command) -> None:
        """
        """
        cmd = command(self)
        if hasattr(command, "SCHEMA"):
            cmd.prepare(db=self.db)
        self.add_cog(cmd)

    def run(self) -> None:
        """
        """
        super().run(self.token)