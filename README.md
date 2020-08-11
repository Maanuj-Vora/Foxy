# Foxy

 
A basic discord bot heavily influenced by [discord_bot.py](https://github.com/AlexFlipnote/discord_bot.py).

---

## Features

* [x] Get An Image of A Foxy, Meow, and Woof
* [x] Specific Admin Commands(Only shown in code)
* [x] Specific Moderator Commands(Shown in help message)
* [x] Greet New Members and Say Goodbye

---

## Table of Commands

| Cog          | Command                  | Description                                                           |
|--------------|--------------------------|-----------------------------------------------------------------------|
| Admin        | amiadmin                 | Are you an admin?                                                     |
| Admin        | load <name>              | Loads an extension.                                                   |
| Admin        | unload <name>            | Unloads an extension.                                                 |
| Admin        | reload <name>            | Reloads an extension.                                                 |
| Admin        | reloadall                | Reloads all extensions.                                               |
| Admin        | reloadutils <name>       | Reloads a utils module.                                               |
| Admin        | reboot                   | Reboot the bot                                                        |
| Admin        | dm <user_id> [message]   | Direct message the user of your choice                                |
| Animal       | foxy                     | Get an image of a foxy                                                |
| Animal       | woof                     | Get an image of a Woof                                                |
| Animal       | meow                     | Get an image of a Meow                                                |
| Discord Info | avatar <user>            | Get the avatar of you or someone else                                 |
| Discord Info | joinedat <user>          | Check when a user joined the current server                           |
| Discord Info | mods                     | Check which mods are online on current guild                          |
| Discord Info | roles                    | Get all roles in current server                                       |
| Discord Info | server                   | Check info about current server                                       |
| Discord Info | server avatar            | Get the current server icon                                           |
| Discord Info | server banner            | Get the current banner image                                          |
| Discord Info | user <user>              | Get user information                                                  |
| Fun          | chucknorris              | Get a Chuck Norris Joke                                               |
| Fun          | 8ball <question>         | Consult the supreme, all knowing 8ball to receive an answer           |
| Information  | about                    | About the bot                                                         |
| Information  | invite                   | Invite me to your server                                              |
| Information  | ping                     | Pong!                                                                 |
| Moderator    | announcerole <role>      | Makes a role mentionable and removes it whenever you mention the role |
| Moderator    | ban <user> [reason]      | Bans a user from the current server                                   |
| Moderator    | find                     | Finds a user within your search term                                  |
| Moderator    | kick <user> [reason]     | Kicks a user from the current server                                  |
| Moderator    | massban <reason> [users] | Mass bans multiple members from the server                            |
| Moderator    | mute <user> [reason]     | Mutes a user from the current server                                  |
| Moderator    | nickname <user> [name]   | Nicknames a user from the current server                              |
| Moderator    | prune all                | Removes all messages                                                  |
| Moderator    | prune bots <prefix>      | Removes a bot user's messages and messages with their optional prefix |
| Moderator    | prune contains <string>  | Removes all messages containing a substring                           |
| Moderator    | prune embeds             | Removes messages that have embeds in them                             |
| Moderator    | prune emojis             | Removes all messages containing custom emoji                          |
| Moderator    | prune files              | Removes messages that have attachments in them                        |
| Moderator    | prune images             | Removes messages that have embeds or attachments                      |
| Moderator    | prune mentions           | Removes messages that have mentions in them                           |
| Moderator    | unban <user> [reason]    | Unbans a user from the current server                                 |
| Moderator    | unmute <user> [reason]   | Unmutes a user from the current server                                |
| News         | news <number>            | Gets The Top News Articles From Google News                           |
| No Category  | help                     | Show the help message                                                 |

---

## Installation

1. Create a virtual environment using the command `virtualenv -p python3 venv` and then activate the virtual environment by doing `.\venv\Scripts\activate`
2. Install `requirements.txt` using pip via `pip3 install -r requirements.txt`
3. Rename the `example.config.json` file to `config.json` and fill in the fields
4. run `main.py` and hope for the best

---

### Please Read

Please keep my account id in the owners in `config.json`
