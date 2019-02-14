from .client import Client
from .bot import Bot
import config


def run():
    if config.bot:
        sc = Bot()
    else:
        sc = Client()
    sc.response = config.response
    sc.status = config.status
    sc.command_prefix = config.command_prefix
    sc.run(config.token)


if __name__ == "__main__":
    run()
