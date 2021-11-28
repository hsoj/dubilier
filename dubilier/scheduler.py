"""
"""


import datetime
import discord.ext.commands
from . import (
    db,
    commands,
)

class Command(db.Mixin,
              commands.Command):
    """
    """
    SCHEMA = """CREATE TABLE IF NOT EXISTS scheule (
        id integer PRIMARY KEY,
        name text,
        notify text,
    );

    CREATE TABLE IF NOT EXISTS schedule_day (
        id integer PRIMARY KEY,
        schedule integer,
        day text,
        time text
    );

    CREATE TABLE IF NOT EXISTS schedule_field (
        id integer PRIMARY KEY,
        schedule integer,
        name text,
        value text
    );
    """

    def _build_time_tag(self, timestamp: str) -> str:
        """
        """
        time_tag = "<t:{time}:F>".format(time=timestamp)
        return time_tag

    @discord.ext.commands.command()
    async def schedule(self, ctx, sub_command: str, configs: str) -> None:
        """
        ?schedule create {name} {notify}
        ?schedule day {name} {day} {time}
        """

    @discord.ext.commands.command()
    async def time(self, ctx) -> None:
        """
        """
        out_msg = "The time is {tag}"
        time_str = datetime.datetime.now().strftime("%s")
        time_tag = self._build_time_tag(timestamp=time_str)
        await ctx.send(out_msg.format(tag=time_tag))

