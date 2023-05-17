import random


def respond(msg: str) -> str:
    message = msg.lower()
    greetings = ['wassup', 'wsg', 'sheesh']
    trolls = ['bruh', 'boi', 'stfu', 'no u']

    if message == 'hi' or message == 'hello':
        return random.choice(greetings)

    if message == 'ur mom':
        return random.choice(trolls)
