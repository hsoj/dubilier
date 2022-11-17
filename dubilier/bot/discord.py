"""Objects dealing with communicating to Discord as a bot."""
# pylint: disable=too-few-public-methods


import importlib.abc
import importlib.machinery
import importlib.resources
import importlib.util
import typing

import discord
import discord.ext.commands
import discord.flags


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

    def find_extensions(self, package: str) -> list[str]:
        """Finds extension modules within the provided package.

        Arguments
            package(str): Package to find extensions in

        Returns:
            list[str]: List of extensions found in the provided package
        """
        extensions: list[str] = []
        contents: typing.Iterator[str] = importlib.resources.contents(package)
        modules: list[str] = self.extract_extension_modules(
            contents=list(contents),
        )
        extensions = [f"{package}.{x}" for x in modules]
        return extensions

    def extract_extension_modules(self, contents: list[str]) -> list[str]:
        """Cleans up the provided contents input to determine the names
        of the extension modules.

        Arguments:
            contents(list[str]): The contents found within the package.

        Returns:
            list[str]: List of actual extension modules.
        """
        modules: list[str] = []
        for content in contents:
            if "__" not in content:
                modules.append(content.replace(".py", ""))
        return modules

    async def setup_hook(self) -> None:
        """Hook method that is executed when the bot is ran which sets
        up all of the extensions that need to be loaded.
        """
        await self.load_extension("dubilier.commands.example")
