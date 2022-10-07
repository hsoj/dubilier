"""Objects dealing with communicating to Discord as a bot."""
# pylint: disable=too-few-public-methods

import typing
import discord
import discord.flags
import discord.ext.commands


class Daemon:
    """Provide the connection to discord and maintain it."""
    DEFAULT_PREFIX: str = "?"

    def __init__(self, token: str, **kwargs: str) -> None:
        """Initializes the dubilier.bot.discord.Daemon object."""
        super().__init__()
        self._bot: typing.Optional[discord.ext.commands.Bot] = None
        self.token: str = token
        self.prefix: str = kwargs.get("prefix", self.DEFAULT_PREFIX)

    @property
    def bot(self) -> discord.ext.commands.Bot:
        """Property method to lazy load the Discord Bot object."""
        if self._bot is None:
            intents: discord.flags.Intents = discord.Intents.all()
            self._bot = discord.ext.commands.Bot(command_prefix=self.prefix,
                                                 intents=intents)
        return self._bot

    def run(self) -> None:
        """Initializes the daemon process."""
        self.bot.run(self.token)
