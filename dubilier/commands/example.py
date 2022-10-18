"""Example Discord bot command"""


import typing
import discord.ext.commands
import dubilier.bot.command


class Command(dubilier.bot.command.Base):
    """An example cog object to test actual execution of the bot.
    """

    @discord.ext.commands.command()
    async def example(self,
                      ctx: discord.ext.commands.Context[typing.Any]) -> None:
        """An example command to demonstrate structure for adding
        functionality to the bot.

        Arguments:
            ctx(discord.ext.commands.Context[typing.Any]):
                Context of the message.
        """
        await ctx.send("boop")


# NOTE: This is fucking whack
async def setup(bot: discord.ext.commands.Bot) -> None:
    """Played out setup method that is required to register a cog"""
    await bot.add_cog(Command(bot))
