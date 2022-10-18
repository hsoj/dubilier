"""Objects dealing with communicating to Discord as a bot."""
# pylint: disable=too-few-public-methods


import typing
import discord
import discord.flags
import discord.ext.commands


class Daemon(discord.ext.commands.Bot):
    """Provide the connection to discord and maintain it."""
    DEFAULT_PREFIX: str = "?"

    def __init__(self, token: str, **kwargs: str) -> None:
        """Initializes the dubilier.bot.discord.Daemon object."""
        super().__init__(
            command_prefix=kwargs.get("prefix", self.DEFAULT_PREFIX),
            intents=discord.Intents.all(),
        )
        self.token: str = token

    def run(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """Initializes the daemon process."""
        super().run(self.token, *args, **kwargs)

    async def setup_hook(self) -> None:
        """Hook method that is executed when the bot is ran which sets
        sets up all of the extensions that need to be loaded.
        """
        await self.load_extension("dubilier.commands.example")
