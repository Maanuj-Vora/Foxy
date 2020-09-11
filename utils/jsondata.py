import requests

jsonUrl = 'https://maanuj-vora.github.io/Foxy/data.json'

def getDeveloper():
    response = requests.get(jsonUrl)
    if response.status_code != 200:
        developer = "Rainbwshep#4828"
    else:
        json = response.json()
        developer = json['developer']
    return developer

def getInvite():
    response = requests.get(jsonUrl)
    if response.status_code != 200:
        invite = None
    else:
        json = response.json()
        invite = json['invite']
    return invite

def getBotInvite():
    response = requests.get(jsonUrl)
    if response.status_code != 200:
        botInvite = None
    else:
        json = response.json()
        invite = json['botInvite']
    return invite

def getBasicMongo():
    response = requests.get(jsonUrl)
    if response.status_code != 200:
        mongoBase = None
    else:
        json = response.json()
        mongoBase = json['mongoBase']
    return mongoBase