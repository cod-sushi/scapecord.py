import discord
from discord.ext import commands
import config


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        kwargs["status"] = discord.Status.do_not_disturb
        kwargs["command_prefix"] = config.command_prefix
        super().__init__(*args, **kwargs)

    async def invoke(self, ctx):
        if ctx.invoked_with:
            await ctx.send(config.response)

    async def on_message(self, message):
        # bot?
        if message.author.bot:
            return
        # mention?
        if self.user.mentioned_in(message):
            await message.channel.send(config.response)
            return
        # invoke command
        await self.process_commands(message)
