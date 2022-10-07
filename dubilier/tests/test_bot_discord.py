# pylint: disable=missing-docstring


import unittest
import unittest.mock
import discord.ext.commands
import dubilier.bot.discord


class TestDaemon(unittest.TestCase):

    def test_bot_constructor(self) -> None:
        daemon: dubilier.bot.discord.Daemon = dubilier.bot.discord.Daemon(
            token="token"
        )
        self.assertIsInstance(daemon.bot, discord.ext.commands.Bot)

    def test_command_prefix(self) -> None:
        expected_prefix: str = "!"
        daemon: dubilier.bot.discord.Daemon
        daemon = dubilier.bot.discord.Daemon(token="token", prefix="!")
        self.assertEqual(expected_prefix, daemon.prefix)

    @unittest.mock.patch("discord.ext.commands.Bot")
    def test_run(self, mock: unittest.mock.Mock) -> None:
        daemon: dubilier.bot.discord.Daemon = dubilier.bot.discord.Daemon(
            token="token"
        )
        daemon.run()
        bot_mock: unittest.mock.Mock = mock.return_value
        bot_mock.run.assert_called_once_with(daemon.token)
