import os

from utils import default, mongo
from utils.data import Bot, HelpFormat
import pymongo

config = default.get("config.json")

print("...Attempting to Login...")

bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=HelpFormat()
)

for file in os.listdir("cogs/active"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.active.{name}")

if config.dbOn:
    mongo.instantiate()

bot.run(config.token)
