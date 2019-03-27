from .client import Client
from .bot import Bot
import config
import discord


def run():
    st = discord.Status.do_not_disturb
    if config.bot_command_prefix:
        scapecord = Bot(config.bot_command_prefix, status=st)
    else:
        scapecord = Client(status=st)

    scapecord.run(config.token)
