#!/usr/bin/env python3
"""
"""


import os
import logging
import argparse
import dubilier.bot
import dubilier.user
import dubilier.scheduler


def load_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    """
    parser.add_argument("-p",
                        dest="path",
                        default=os.environ.get("DUBILIER_PATH", None),
                        help="Path to the sqlite database")
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
    dub = dubilier.bot.Bot(db_path=args.path,
                           token=args.token)
    dub.add_cmd(dubilier.scheduler.Command)
    dub.add_cmd(dubilier.user.Command)
    dub.run()


if __name__ == "__main__":
    main()
