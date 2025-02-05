import discord
from settings import OWNER_ID

def isDM(message) :
    return (type(message.channel) == discord.DMChannel)

def hasPrefix(message, prefix) :
    chars = len(prefix)
    if(chars == 0) : return True
    if(message.content[:chars] == prefix) : return True
    return False

def userInActiveGame(aID, games) :
    # get the channel ID of the active game a user is in
    active = [ k for k,v in games.items() if v["game"].hasUser(aID) ]

    if len(active) == 1 :
        return active[0]
    else :
        return False

def canManageGuild(author, guild) :
    guildOwner = guild.owner == author
    guildAdmin = author.guild_permissions.administrator
    guildManager = author.guild_permissions.manage_guild

    return guildOwner or guildAdmin or guildManager

def guildsUserCanManage(author, guilds) :
    active = [ g.id for g in guilds if canManageGuild(author) ]
    return active

def parseMessage(message, prefix) :
    args = message.content.split(" ")
    args[0] = args[0][len(prefix):]
    command = args[0].lower()

    return command, args

class Colours :
    DEFAULT = 0
    AQUA = 1752220
    GREEN = 3066993
    BLUE = 3447003
    PURPLE = 10181046
    GOLD = 15844367
    ORANGE = 15105570
    RED = 15158332
    GREY = 9807270
    DARKER_GREY = 8359053
    NAVY = 3426654
    DARK_AQUA = 1146986
    DARK_GREEN = 2067276
    DARK_BLUE = 2123412
    DARK_PURPLE = 7419530
    DARK_GOLD = 12745742
    DARK_ORANGE = 11027200
    DARK_RED = 10038562
    DARK_GREY = 9936031
    LIGHT_GREY = 12370112
    DARK_NAVY = 2899536
    LUMINOUS_VIVID_PINK = 16580705
    DARK_VIVID_PINK = 12320855
