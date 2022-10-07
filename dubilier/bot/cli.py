"""The primary CLI group for the bot entry point"""


import click


@click.group()
@click.pass_context
def main() -> None:
    """Main CLI group"""


# pylint: disable=unused-argument
@main.command()
@click.option("-db", default=None, help="Path to the sqlite database")
@click.option("-t", default=None, help="Token to auth to Discord")
@click.pass_context
def run(db_path: str, token: str) -> None:
    """Start the bot daemon"""
