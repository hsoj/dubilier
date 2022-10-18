# pylint: disable=missing-docstring


import unittest
import unittest.mock
import discord.ext.commands
import dubilier.bot.command


class TestBase(unittest.TestCase):

    def setUp(self) -> None:
        bot_mock: unittest.mock.Mock = unittest.mock.Mock()
        self.command: dubilier.bot.command.Base = dubilier.bot.command.Base(
            bot=bot_mock,
        )

    def test_constructor(self) -> None:
        self.assertIsInstance(self.command, discord.ext.commands.Cog)
