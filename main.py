import discord
from discord.ext import commands
import keyboard


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("bot is ready.")
    await client.change_presence(activity=discord.Game('Being a fucking idiot, like usual.'))

@client.command()
async def up(ctx):
    await ctx.send("input up")
    keyboard.press('w')

@client.command()
async def left(ctx):
    await ctx.send("input left")
    keyboard.press('a')

@client.command()
async def down(ctx):
    await ctx.send("input down")
    keyboard.press('s')

@client.command()
async def right(ctx):
    await ctx.send("input right")
    keyboard.press('d')

@client.command()
async def select(ctx):
    await ctx.send("input select")
    keyboard.press('z')

@client.command()
async def start(ctx):
    await ctx.send("input select")
    keyboard.press('x')

@client.command()
async def a(ctx):
    await ctx.send("input A button")
    keyboard.press('n')

@client.command()
async def b(ctx):
    await ctx.send("input B button")
    keyboard.press('M')

client.run('What you looking for :)')



