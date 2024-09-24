from discord.ext import commands
from discord import app_commands
import discord
import random
import datetime
import pytz

with open('token.txt') as f:
    BOT_TOKEN = f.read()
CHANNEL_ID = 1076857187198046370
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix="l!", intents=discord.Intents.all())

class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot


@bot.event
async def on_ready():
    print('qq')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)}")
    except Exception as e:
        print(e)

@bot.tree.command(name="random")
@app_commands.describe(arg = "max number")
async def say(interaction: discord.Integration, arg: int):
    randnum = random.randint(0,arg)
    numlist = str(randnum)
    await interaction.response.send_message(str(numlist) + '/' + str(arg))

@bot.tree.command(name="roll")
async def say(interaction: discord.Integration):
    randnum = random.randint(0,100)
    numlist = str(randnum)
    if len(numlist) == 1: numlist = '00' + numlist
    if len(numlist) == 2: numlist = '0' + numlist
    if len(numlist) == 3: numlist = numlist
    await interaction.response.send_message(str(numlist))

@bot.tree.command(name="ddos")
@app_commands.describe(arg = "max number")
async def say(interaction: discord.Integration, arg: int):
    channel = interaction.channel
    for n in range(0,arg):
        await channel.send('https://media.tenor.com/Fri8F_tkuhgAAAAC/%D1%81%D0%BF%D0%BE%D0%BA%D0%BE%D0%B9%D0%BD%D0%BE%D0%B9%D0%BD%D0%BE%D1%87%D0%B8-good-night.gif')

@bot.tree.command(name="stackcalc")
@app_commands.describe(itemcount = "item count")
async def say(interaction: discord.Integration, itemcount: int):
    embed = discord.Embed(
        color=discord.Color.dark_teal(),
        description=str(itemcount) + ' items',
        title=str(itemcount//64) + ' stacks \n' + str(itemcount%64) + ' items'
    )

    embed.set_author(name='item calculator')
    await interaction.response.send_message(embed=embed)
    #await interaction.response.send_message('`\n' + str(itemcount) + ' items\n--------\n' + str(itemcount//64) + ' stacks \n' + str(itemcount%64) + ' items`')

@bot.tree.command(name="itemcalc")
@app_commands.describe(stackcount = "stack count")
@app_commands.describe(itemcount = "item count")
async def say(interaction: discord.Integration, stackcount: int, itemcount: int):
    embed = discord.Embed(
        color=discord.Color.dark_teal(),
        description=str(stackcount) + ' stacks \n' + str(itemcount) + ' items',
        title=str(stackcount*64+ itemcount) + ' items'
    )

    embed.set_author(name='item calculator')
    await interaction.response.send_message(embed=embed)
    #await interaction.response.send_message('`\n' + str(stackcount) + ' stacks \n' + str(itemcount) + ' items\n--------\n' + str(stackcount*64+ itemcount) + ' items`')


@bot.tree.command(name="poll")
@app_commands.describe(time = "time(secs)")
@app_commands.describe(first_option = "first option")
@app_commands.describe(second_option = "second option")
async def say(interaction: discord.Integration, time: int, first_option: str, second_option: str):
    author = interaction.user.name
    datetime_LT = datetime.datetime.now(pytz.timezone('Europe/Warsaw'))
    date = datetime_LT + datetime.timedelta(seconds=time)
    date = date.strftime("%H:%M:%S")
    embed = discord.Embed(
        color=discord.Color.dark_teal(),
        title=str(first_option) + ' or ' + str(second_option) + '?',
        description=f'ends in {date}'
    )
    embed.set_author(name=f'started by {author}')
    await interaction.response.send_message(embed=embed)


@bot.event
async def on_message(message):
    if message.content == ('лайтли лох'):
        channel = message.channel
        await channel.send('https://media.tenor.com/la6XSsTlvD4AAAAd/the-rock-meme.gif')


bot.run(BOT_TOKEN)