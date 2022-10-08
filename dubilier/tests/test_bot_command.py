# pylint: disable=missing-docstring


import unittest
import unittest.mock
import discord.ext.commands
import dubilier.bot.command


class TestBase(unittest.TestCase):

    def test_constructor(self) -> None:
        command: dubilier.bot.command.Base = dubilier.bot.command.Base()
        self.assertIsInstance(command, discord.ext.commands.Cog)
