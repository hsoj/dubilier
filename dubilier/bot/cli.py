"""The primary CLI group for the bot entry point"""


import click
import dubilier.bot.discord


@click.group(name="bot")
def group() -> None:
    """Commands for dealing with the Dubilier bot."""


# pylint: disable=unused-argument
@group.command()
@click.option("-p", "db_path",
              default=None,
              help="Path to the sqlite database")
@click.option("-t", "token", default=None, help="Token to auth to Discord")
def run(db_path: str, token: str) -> None:
    """Start the bot daemon"""
    daemon: dubilier.bot.discord.Daemon = dubilier.bot.discord.Daemon(
        token=token,
    )
    daemon.run()
