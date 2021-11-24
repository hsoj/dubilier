#!/usr/bin/env python3
"""
"""


import os
import sys
import logging
import argparse
import datetime
import discord.ext.tasks
import discord.ext.commands


class Dubilier(discord.ext.commands.Bot):
    DEFAULT_PREFIX = "!"

    def __init__(self, **kwargs: dict) -> None:
        super().__init__(
            command_prefix=kwargs.get("prefix", self.DEFAULT_PREFIX),
        )
        self.add_cog(Test(self))


class Test(discord.ext.commands.Cog):

    def __init__(self, bot: discord.ext.commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @discord.ext.commands.command()
    async def boop(self, ctx) -> None:
        await ctx.send("boop")

    @discord.ext.commands.command()
    async def set(self, ctx, message: str) -> None:
        """
        """
        

    @discord.ext.commands.command()
    async def time(self, ctx, message: str) -> None:
        """
        """
        if message == "now":
            now = datetime.datetime.now().strftime("%s")
            await ctx.send("The time is <t:{time}:F>".format(time=now))


def load_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    """
    parser.add_argument("-t",
                            dest="token",
                            default=os.environ.get("DUBILIER_TOKEN", None),
                            help="The Discord bot token")
    args = parser.parse_args()
    return args


def main():
    """
    """
    # TODO: Add the logging level as a configurable argument
    logging.basicConfig(level=logging.DEBUG)
    arg_parser = argparse.ArgumentParser(
        description="Dubilier ham bot",
    )
    args = load_args(arg_parser)
    if not args.token:
        print("Error: Missing Discord token")
        sys.exit(1)
    dub = Dubilier()
    dub.run(args.token)


if __name__ == "__main__":
    main()
