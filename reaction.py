import random


def respond(msg: str) -> str:
    message = msg.lower()

    greetings = ['wsg', 'what up', 'yo', 'hyd', 'sheesh']
    trolls = ['bruh', 'boi', 'stfu', 'no u']
    ratios = ['L', 'L + ratio', 'job + ratio', 'counter ratio', 'stfu']

    # sample commands/responses
    if message == 'hello' or message == 'hi':
        return random.choice(greetings)
    elif message == 'ur mom' or message == 'L':
        return random.choice(trolls)
    elif message == 'ratio':
        return random.choice(ratios)
    elif message == '!flight':
        return 'https://tenor.com/view/yummy-tongue-flight-flight-reacts-excited-gif-17057509'
    elif message == '!flight2':
        return 'https://tenor.com/view/flightreacts-cringe-gif-19831193'
    elif message == '!help':
        return '`List of all commands (tbd)`'
