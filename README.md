# scapecord.py
scapecord.py is a "construction sign" discord bot written in discord.py.

When your bot is under maintenance, This bot becomes a "Scapegoat".

- Set bot state "Do not disturb"
- Send custom response when the bot is mensioned
- Apply to both mention and custom prefix-command(ex: $start, $help, etc)


# Usage

## Clone this repository

```
$ git clone git@github.com:cod-sushi/scapecord.py.git
```

## Install dependencies

```
$ cd scapecord.py
$ pip install -r requirement.txt
```

## Set up configuration

Edit config.py and place in the bot's root directory.

```python
# config.py
# coding: UTF-8
import discord

status = discord.Status.do_not_disturb
token = 'YOUR_DISCORD_TOKEN'
response = "Sorry, I'm down for maintenance now. Please wait a moment."
bot = True
command_prefix = '$'
```
Make the following folder structure:
```
examples
├── config.py
└── sample.py
```

## run sample.py
```
$ python sample.py
```




