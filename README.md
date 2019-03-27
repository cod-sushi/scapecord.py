# scapecord.py
scapecord.py is a "construction sign" discord bot written in discord.py.

When your bot is under maintenance, This bot becomes a "Scapegoat".

- Set bot state "Do not disturb"
- Send custom response when the bot is mensioned
- Apply to both mention and custom prefix-command(ex: $start, $help, etc)

# Example

## Code

### config.py
```python
# coding: UTF-8
token = 'YOUR_DISCORD_TOKEN'
response = "Sorry, I'm down for maintenance now. Please wait a moment."
bot_command_prefix = '$'
```

### main.py
```python
# coding: UTF-8
import scapecord
scapecord.run()
```

## ScreenShot



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

### Edit config.py.

```shell
$ cd scapecord/
$ cp config.py.sample config.py
```

```python
# config.py
# coding: UTF-8

token = 'YOUR_DISCORD_TOKEN'
response = "Sorry, I'm down for maintenance now. Please wait a moment."
# If your bot is discord.ext.commands.Bot:
bot_command_prefix = '$'
# If your bot is discord.Client:
bot_command_prefix = None
```

### create main python file
```shell
$ vim main.py
```

```python
# coding: UTF-8
import scapecord

scapecord.run()
```

### run 
```
$ python main.py
```
