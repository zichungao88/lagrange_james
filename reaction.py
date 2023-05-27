import random


def respond(msg: str) -> str:
    message = msg.lower()

    commands = ['help',
                'flight',
                'flight2']
    responses = ['```List of all commands (tbd)```',
                 'https://tenor.com/view/yummy-tongue-flight-flight-reacts-excited-gif-17057509',
                 'https://tenor.com/view/flightreacts-cringe-gif-19831193']

    greetings = ['wsg', 'what up', 'yo', 'hyd', 'sheesh', ':smile:']
    trolls = ['bruh', 'boi', 'stfu', 'no u', ':clown:']
    ratios = ['L', 'L + ratio', 'job + ratio', 'counter ratio', 'stfu', ':clown:']

    if message[0] == '/':
        if message[1:] in commands:
            return responses[commands.index(message[1:])]
        else:
            return 'Command not found'
    else:
        if message == 'hello' or message == 'hi':
            return random.choice(greetings)
        elif message == 'ur mom' or message == 'L':
            return random.choice(trolls)
        elif message == 'ratio':
            return random.choice(ratios)
