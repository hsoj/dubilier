# pylint: disable=missing-docstring


import unittest
import unittest.mock
import discord.ext.commands
import dubilier.bot.command


class TestBase(unittest.TestCase):

    def setUp(self) -> None:
        self.command: dubilier.bot.command.Base = dubilier.bot.command.Base()

    def test_constructor(self) -> None:
        self.assertIsInstance(self.command, discord.ext.commands.Cog)
