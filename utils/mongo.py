import pymongo
from utils import default, jsondata

mongo = None


def instantiate():
    global mongo

    config = default.get("config.json")
    DB_URI = config.dburi

    mongo = pymongo.MongoClient(DB_URI)


def useDB():
    config = default.get("config.json")
    return bool(config.dbOn)


def addGuild(guild):
    global mongo

    data = mongo.db.dataBase

    if data.find_one({'guildID': guild.id}) == None:
        data.insert({'guildID': guild.id, 'guildName': guild.name})

    currGuild = data.find_one({'guildID': guild.id})

    baseMongo = jsondata.getBasicMongo()
    missingItems = {}
    needToAddItems = False
    for key, value in baseMongo.items():
        if key not in currGuild:
            if value == 'True' or value == 'False':
                missingItems[key] = not bool(value)
            else:
                missingItems[key] = value
            needToAddItems = True

    if needToAddItems:
        data.update_one({
            'guildID': guild.id
        },
            {'$set': missingItems}, upsert=False)


def checkMemberEntry(guild):
    data = mongo.db.dataBase
    return (data.find_one({'guildID': guild.id}))['onMemberEntry']


def getMemberEntryMessage(guild):
    data = mongo.db.dataBase
    return (data.find_one({'guildID': guild.id}))['welcome']


def toggleMemberEntry(guild):
    data = mongo.db.dataBase
    toggledCurr = not (data.find_one({'guildID': guild.id}))['onMemberEntry']
    data.update_one({
        'guildID': guild.id
    },
        {'$set': {'onMemberEntry': toggledCurr}}, upsert=False)
    return f"When a new user joins, welcome message will be shown: **{toggledCurr}**"


def changeMemberEntryMessage(guild, message):
    data = mongo.db.dataBase
    data.update_one({
        'guildID': guild.id
    },
        {'$set': {'welcome': message}}, upsert=False)
    return f"When a new user joins, this welcome message will be shown:\n{message}"


def checkMemberLeave(guild):
    data = mongo.db.dataBase
    return (data.find_one({'guildID': guild.id}))['onMemberLeave']


def getMemberLeaveMessage(guild):
    data = mongo.db.dataBase
    return (data.find_one({'guildID': guild.id}))['leave']


def toggleMemberLeave(guild):
    data = mongo.db.dataBase
    toggledCurr = not (data.find_one({'guildID': guild.id}))['onMemberLeave']
    data.update_one({
        'guildID': guild.id
    },
        {'$set': {'onMemberLeave': toggledCurr}}, upsert=False)
    return f"When an user leaves, goodbye message will be shown: **{toggledCurr}**"


def changeMemberLeaveMessage(guild, message):
    data = mongo.db.dataBase
    data.update_one({
        'guildID': guild.id
    },
        {'$set': {'leave': message}}, upsert=False)
    return f"When an user leaves, this goodbye message will be shown:\n{message}"
