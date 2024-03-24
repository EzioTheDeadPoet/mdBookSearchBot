import discord
import json


bot = discord.Bot()


@bot.command()
# pycord will figure out the types for you
async def add(ctx, query: discord.Option(str)):
    await ctx.respond(f"The sum of {first} and {second} is {sum}.")


bot.run("TOKEN")
