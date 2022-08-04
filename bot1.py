import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send(f'{message.author.mention}Hello!')

client.run('MTAwNDgxNzgxMDk2ODU0MzM5NQ.Gfj7DF.7Q2X7uyGnSo0zK9HbEjYaNthTCxRt_-43XSeU4')