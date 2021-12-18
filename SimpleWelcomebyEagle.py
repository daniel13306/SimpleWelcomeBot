import discord
from discord.ext import commands
import datetime
from datetime import datetime
import asyncio
from discord.utils import get

# By DeadEagle
#
# www.Coding-Community.com
#
# https://discord.gg/FTmrYbEN8w


### Token / Welcome Channel ID ###
TOKEN = "Enter_Your_Bot_Token"

WelcomeChannelID = int("Enter_Your_WelcomeChannel_ID")
###                            ###

## Make sure to Enable Intents, Read the Readme.
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)




@client.event
async  def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Welcome Bot"))






@client.event
async def on_member_join(member):
    print('Member Joined!')
    # Calls WelcomeMessage Function [Down Below]
    await WelcomeMessage(member)

@client.event
async def on_member_remove(member):
    print('Member Left')
    # Perform actions on Member Leave
    pass


@client.event
async def on_message(message):
    # Perform actions on_Message
    pass



async def WelcomeMessage(member):
    channel = client.get_channel(WelcomeChannelID)
    MemberID = str(member.id)
    MemberMention = "<@!"+MemberID+">"
    # Welcome Message Defined Below.
    WelcomeMessage =  "Welcome to the Server "+MemberMention+"!"
    #                   ^
    await channel.send(WelcomeMessage)



client.run(TOKEN)