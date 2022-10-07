"""The primary CLI group for the bot entry point"""


import click


@click.group()
def cli() -> None:
    """Main CLI group"""
