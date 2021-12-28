import discord
from discord.ext import commands
from random import randint
import asyncio

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('$info for help'))
    print('RPS Bot is ready')

@bot.command(aliases=['info'])
async def _help(ctx):
    await ctx.send("To use this bot, do $rock, $paper or $scissors for a chance to win!")


#rock = 0, paper = 1, scissors = 2


@bot.command()
async def rock(ctx):
    bot_choice = randint(0,2)
    
    if bot_choice == 0:
        await ctx.send("Bot also chose rock! Tie!")

    elif bot_choice == 1:
        await ctx.send("Bot chose scissors! You win!")
        
    elif bot_choice == 2:
        await ctx.send("Bot chose paper! You lose!")

@bot.command()
async def paper(ctx):
    bot_choice = randint(0,2)
    
    if bot_choice == 0:
        await ctx.send("Bot chose rock! You win!")

    elif bot_choice == 1:
        await ctx.send("Bot chose scissors! You lose!")
        
    elif bot_choice == 2:
        await ctx.send("Bot also chose paper! Tie!")

@bot.command()
async def scissors(ctx):
    bot_choice = randint(0,2)
    
    if bot_choice == 0:
        await ctx.send("Bot chose rock! You lose!")

    elif bot_choice == 1:
        await ctx.send("Bot also chose scissors! Tie!")
        
    elif bot_choice == 2:
        await ctx.send("Bot chose paper! You win!")

bot.run('YOUR_DISCORD_TOKEN')