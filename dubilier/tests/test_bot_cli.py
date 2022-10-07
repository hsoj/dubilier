# pylint: disable=missing-docstring


import unittest
import unittest.mock
import click.testing
import dubilier.cli

class TestBotCLI(unittest.TestCase):

    @unittest.mock.patch("discord.ext.commands.Bot")
    def test_run(self, mock: unittest.mock.Mock) -> None:
        args: list[str] = [
            "bot",
            "run",
            "-p test_db_path",
            "-t test_token",
        ]
        runner: click.testing.CliRunner = click.testing.CliRunner()
        result: click.testing.Result = runner.invoke(dubilier.cli.main,
                                                     args)
        bot_mock: unittest.mock.Mock = mock.return_value
        bot_mock.run.exit_code = 0
        self.assertEqual(result.exit_code, 0)
