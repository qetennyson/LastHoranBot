import random
import requests
from discord.ext.commands import Bot
from fortunes import horans

BOT_PREFIX = ("?", "!")
TOKEN = "PLACEHOLDER.PLACEHOLDING.HELD"

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name="horans", description="Hear a classic line from Mr. Horan!",
                brief="Provide s a Horan saying.",
                aliases=["horan", "mrhoran", "mr.horan"],
                pass_context=True)
async def fortune_cookie(context):
    await client.say(context.message.author.mention + " LISTEN UP " + random.choice(horans))
    await client.say("......#@$ASsd4##vjgtgcnjqtcpncp##!@AS8as89#.......2")


@client.command(name="dadjoke", description="The latest dadjokes all in one place.",
                brief="You will receive one AMAZING dadjoke, HA-HA :-)")
async def dad_joke():
    headers = {'Accept': 'application/json'}
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers=headers)
    joke = response.json()['joke']
    await client.say(str(joke))

client.remove_command('help')
@client.command(description="Command: vjgtgcnjqtcpncp - Et tu brute",
                brief="A strange command that seems to serve no purpose as is.",
                aliases=["therealhoranlan"], pass_context=True)
async def bingbong(context):
    await client.say(context.message.author.mention + " .. what a curious mind you have.  Come see "
                                                      "Mr. Tennyson for an adventure.")

@client.command(description="Make a crazy announcement when someone earns a snack.",
                brief="read the description", aliases=["snack"])

async def snack_announcement():
    await client.say("SOMEONE JUST EARNED A SNACK, PLAY DARUDE SANDSTORM GRANT.")

@client.command(description="Mr. Horan eats peanut butter.", brief="Yep",
                aliases=["peanutbutter", "pb", "pbhoran"])
async def horan_pb():
    await client.say("Mr. Horan consumes peanut butter.")
    await client.say("Peanut Butter was originally created by George Washington Carver")
    await client.say("PSYCH, it was actually invented by Canadian "
                     " pharmacist Marcellus Gilmore Edson")
    await client.say("Mr. Horan consumes more peanut butter.  Violently.")

client.run(TOKEN)
