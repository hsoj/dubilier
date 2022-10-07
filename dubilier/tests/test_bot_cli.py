# pylint: disable=missing-docstring


import unittest
import click.testing
import dubilier.bot.cli

class TestBotCLI(unittest.TestCase):

    def test_run(self) -> None:
        runner: click.testing.CliRunner = click.testing.CliRunner()
        result: click.testing.Result = runner.invoke(dubilier.bot.cli.run,
                                                     None,
                                                     None)
        self.assertEqual(result.exit_code, 1)
