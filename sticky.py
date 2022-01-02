import discord
from discord.ext import commands
import sqlite3

# Connect to DB
def connectDB():
    connection = sqlite3.connect('mcCoords.db')
    cursor = connection.cursor()
    return connection, cursor


# Close DB connection
def closeDB(connection):
    connection.commit()
    connection.close()

# Create bot client
token = open("token.txt", "r").read()
sticky = commands.Bot(command_prefix="!")

# Connect with bot
@sticky.event
async def on_ready():
    print("Ready to go!")


## MC Database commands ##

# Get list of coordinates
@sticky.command()
async def xy(ctx):
    print("Working xy")
    conn, curs = connectDB()
    curs.execute("SELECT * FROM mcLocations")
    results = "Location Name\tX\tY\n"
    for item in curs.fetchall():
        results += str(item) +"\n"
    await ctx.channel.send(results)

# Add coordinate to coordinate list
@sticky.command()
async def add(ctx, *arg):
    print("Working add")
    if len(arg) != 2:
        await ctx.send("Try adding a coordinate like this:\n" +
            "\t'!add locationName xCoord yCoord'")
    else:
        pass

# Remove coordinate from coordinate list
@sticky.command()
async def rm(ctx, locationName = None):
    if(locationName and len(locationName) == 1):
        print("yuh")
    else:
        await ctx.send("Try removing a location like this: \n" +
            "\t'!rm locationName'")


## Bot Commands ##


# Remove iFunny links
@sticky.listen('on_message')
async def noFunnyLinks(msg):
    if "ifunny" in msg.content.lower() and not msg.content.startswith("!"):
        await msg.delete()






# Run bot client
sticky.run(token)