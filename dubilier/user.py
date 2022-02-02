"""
"""


import logging
import sqlalchemy
import discord.ext.commands
from . import (
    db,
    commands,
)


class User(db.Mixin,
           db.Base):
    """
    """
    discord_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    call_sign = sqlalchemy.Column(sqlalchemy.String)


class Command(commands.Command):
    """
    """

    def _user(self, discord_id: int) -> User:
        """
        """
        user = self.db.get(User, discord_id=discord_id).first()
        if user is None:
            user = self.db.insert(User(discord_id=discord_id))
        return user

    async def user_callsign(self, ctx, *args: list) -> None:
        """
        """
        user = self._user(discord_id=ctx.author.id)
        if not len(args):
            await ctx.send("No callsign provided")
            return None
        user.call_sign = args[0]
        user = self.db.update(user)
        await ctx.send("Added callsign: {callsign}".format(
            callsign=user.call_sign,
        ))

    async def user_get(self, ctx, *args: list) -> None:
        """
        """
        user = self._user(discord_id=ctx.author.id)
        if user.call_sign is None:
            await ctx.send(
                "User has no call-sign (insert text on adding here)"
            )

    @discord.ext.commands.command()
    async def user(self, ctx, sub_command: str, *args) -> None:
        """
        """
        command = "user_{sub_command}".format(sub_command=sub_command)
        logging.info("Calling command: {command} {args}".format(
            command=command,
            args=args,
            ))
        if hasattr(self, command):
            method = getattr(self, command)
            results = await method(ctx, *args)