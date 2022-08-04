# MTAwNDgxNzgxMDk2ODU0MzM5NQ.Gfj7DF.7Q2X7uyGnSo0zK9HbEjYaNthTCxRt_-43XSeU4
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTAwNDgxNzgxMDk2ODU0MzM5NQ.Gfj7DF.7Q2X7uyGnSo0zK9HbEjYaNthTCxRt_-43XSeU4')










# class MyClient(discord.client):
#     async def on_ready(self):
#         print("Loggen on as", self.user)
#
#     async def on_message(self, message):
#         if message.author == self.user:
#             return
#         if message.content == 'ping':
#             await message.chanel.send('pong')
#
#
# client = MyClient()
# client.run('MTAwNDgxNzgxMDk2ODU0MzM5NQ.Gfj7DF.7Q2X7uyGnSo0zK9HbEjYaNthTCxRt_-43XSeU4')
