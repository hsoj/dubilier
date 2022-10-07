# pylint: disable=missing-docstring


import unittest
import click.testing
import dubilier.bot.cli

class TestBotCLI(unittest.TestCase):

    def test_run(self) -> None:
        args: list[str] = [
            "run",
            "-p test_db_path",
            "-t test_token",
        ]
        runner: click.testing.CliRunner = click.testing.CliRunner()
        result: click.testing.Result = runner.invoke(dubilier.bot.cli.main,
                                                     args)
        self.assertEqual(result.exit_code, 0)
