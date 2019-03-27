# scapecord.py
scapecord.py is a "construction sign" discord bot written in discord.py.

![mark_koujichu](https://user-images.githubusercontent.com/46142035/55067106-734fd500-50c2-11e9-8fad-0e751db453bc.png)

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

### Status
![20190327_185215](https://user-images.githubusercontent.com/46142035/55066674-9e85f480-50c1-11e9-9eeb-709c0fa8fbb7.png)
### Conversation 
![20190327_184359](https://user-images.githubusercontent.com/46142035/55066515-5070f100-50c1-11e9-9904-4e6cf6d84b09.png)

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
You can use `example/`. There are sample code and config.py. 

### Create config.py
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

### Create main.py
```shell
$ vim main.py
```

```python
# coding: UTF-8
import scapecord
scapecord.run()
```

### Run 
```
$ python main.py
```
