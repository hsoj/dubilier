"""Objects dealing with communicating to Discord as a bot."""
# pylint: disable=too-few-public-methods

import typing
import discord
import discord.flags
import discord.ext.commands


class Intents(discord.flags.Intents):
    """Extend the discord.Intents object to ensure that proper linting
    is provided.
    """
    __slots__: tuple[str] = ("message_content",)

    def __init__(self) -> None:
        super().__init__()
        self.message_content = super().message_content


class Daemon:
    """Provide the connection to discord and maintain it."""
    DEFAULT_PREFIX: str = "?"

    def __init__(self, **kwargs: str) -> None:
        """Initializes the dubilier.bot.discord.Daemon object."""
        super().__init__()
        self._bot: typing.Optional[discord.ext.commands.Bot] = None
        self.prefix: str = kwargs.get("prefix", self.DEFAULT_PREFIX)

    @property
    def bot(self) -> discord.ext.commands.Bot:
        """Property method to lazy load the Discord Bot object."""
        if self._bot is None:
            intents: Intents = Intents()
            intents.message_content = True
            self._bot = discord.ext.commands.Bot(command_prefix=self.prefix,
                                                 intents=intents)
        return self._bot
