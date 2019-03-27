from discord.ext import commands
import config


class Bot(commands.Bot):
    async def invoke(self, ctx):
        if self.user.mentioned_in(ctx.message):
            # Mention was processed in on_message.
            return

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
