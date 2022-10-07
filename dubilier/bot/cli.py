"""The primary CLI group for the bot entry point"""


import click


@click.group()
@click.pass_context
def cli() -> None:
    """Main CLI group"""


@cli.command()
@click.option("-db", default=None, help="Path to the sqlite database")
@click.option("-t", default=None, help="Token to auth to Discord")
@click.pass_context
def run(db: str, token: str) -> None:
    """Start the bot daemon"""
