"""Main entrypoint for Dubilier."""


import click
import dubilier.bot.cli


@click.group()
def main() -> None:
    """Interact with the Dubilier bot."""

main.add_command(dubilier.bot.cli.group)
