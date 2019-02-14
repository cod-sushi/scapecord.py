import discord
import config


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        kwargs["status"] = config.status
        super().__init__(*args, **kwargs)

    async def on_message(self, message):
        # bot?
        if message.author.bot:
            return
        # mention?
        if self.user.mentioned_in(message):
            await message.channel.send(config.response)
