# pylint: disable=missing-docstring


import unittest
import discord.ext.commands
import dubilier.bot.discord


class TestDaemon(unittest.TestCase):

    def test_bot_constructor(self) -> None:
        daemon: dubilier.bot.discord.Daemon = dubilier.bot.discord.Daemon()
        self.assertIsInstance(daemon.bot, discord.ext.commands.Bot)

    def test_command_prefix(self) -> None:
        expected_prefix: str = "!"
        daemon: dubilier.bot.discord.Daemon
        daemon = dubilier.bot.discord.Daemon(prefix="!")
        self.assertEqual(expected_prefix, daemon.prefix)
