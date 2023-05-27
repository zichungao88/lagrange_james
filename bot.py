import discord
import reaction


async def message(msg, user_msg, private):
    try:
        response = reaction.respond(user_msg)
        if private:
            await msg.author.send(response)
        else:
            await msg.channel.send(response)

    except Exception as e:
        print(e)


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('LeGM back at it')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return

        user_msg = str(msg.content)

        if user_msg[:2] == 'dm':
            user_msg = user_msg[3:]
            await message(msg, user_msg, private=True)
        else:
            await message(msg, user_msg, private=False)

    with open('token.txt', 'r') as file:
        TOKEN = file.read()

    client.run(TOKEN)
