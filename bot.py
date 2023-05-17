import discord
import reaction


async def send_msg(msg, user_msg, private):
    try:
        response = reaction.respond(user_msg)
        await msg.author.send(response) if private else await msg.channel.send(response)
    except Exception as error:
        print(error)


def run():
    # TOKEN = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def bot_ready():
        print('LeGM back at it')

    @client.event
    async def bot_msg(msg):
        if msg.author == client.user:
            return
        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)
        if user_msg[0] == '!':
            user_msg = user_msg[1:]
            await send_msg(msg, user_msg, private=True)
        else:
            await send_msg(msg, user_msg, private=False)

    client.run(TOKEN)
