import os

from utils import default
from utils.data import Bot, HelpFormat


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


bot.run(config.token)
