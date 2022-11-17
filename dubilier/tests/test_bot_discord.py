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
        self.assertIsInstance(daemon, discord.ext.commands.Bot)

    def test_command_prefix(self) -> None:
        expected_prefix: str = "!"
        daemon: dubilier.bot.discord.Daemon
        daemon = dubilier.bot.discord.Daemon(token="token", prefix="!")
        self.assertEqual(expected_prefix, daemon.command_prefix)

    @unittest.mock.patch("importlib.resources.contents")
    def test_find_extensions(self, content_mock: unittest.mock.MagicMock) -> None:
        package: str = "test.package"
        contents: list[str] = [
            "__init__.py",
            "file_one.py",
            "file_two.py",
        ]
        expected: list[str] = [
            f"{package}.file_one",
            f"{package}.file_two"
        ]
        daemon: dubilier.bot.discord.Daemon
        daemon = dubilier.bot.discord.Daemon(token="token")
        content_mock.return_value = contents
        self.assertEqual(expected, daemon.find_extensions(package))

    def test_extract_extension_modules(self) -> None:
        contents: list[str] = [
            "__init__.py",
            "file_one.py",
            "file_two.py",
        ]
        expected: list[str] = ["file_one", "file_two"]
        daemon: dubilier.bot.discord.Daemon
        daemon = dubilier.bot.discord.Daemon(token="token")
        actual: list[str] = daemon.extract_extension_modules(contents=contents)
        self.assertEqual(expected, actual)
