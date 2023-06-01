import random


def respond(msg: str) -> str:
    message = msg.lower()

    with open('commands.txt', 'r') as command:
        commands = command.read().split('\n')
        commands.pop()

    with open('responses.txt', 'r') as response:
        responses = response.read().split('\n')
        responses.pop()

    with open('greetings.txt', 'r') as greeting:
        greetings = greeting.read().split('\n')
        greetings.pop()

    with open('hypes.txt', 'r') as hype:
        hypes = hype.read().split('\n')
        hypes.pop()

    with open('trolls.txt', 'r') as troll:
        trolls = troll.read().split('\n')
        trolls.pop()

    with open('ratios.txt', 'r') as ratio:
        ratios = ratio.read().split('\n')
        ratios.pop()

    with open('le.txt', 'r') as le:
        gm = le.read().split('\n')
        gm.pop()

    if message[:2] == '//':
        if message[2:] == 'help':
            return '```' \
                   'List of all commands:\n' \
                   '(Note: all commands are in lowercase)\n' \
                   '\n' \
                   'help (shows this message) \n' \
                   'accent\n' \
                   'bowling\n' \
                   'bowling2\n' \
                   'cap\n' \
                   'cri\n' \
                   'daddy\n' \
                   'flight\n' \
                   'flight2\n' \
                   'flight3\n' \
                   'hector\n' \
                   'inertia\n' \
                   'league\n' \
                   'monke\n' \
                   'monke2\n' \
                   'monke3\n' \
                   'monke4\n' \
                   'stop\n' \
                   'wtf\n' \
                   'wtf2\n' \
                   'wtf3\n' \
                   'zina' \
                   '```'
        elif message[2:] in commands:
            return responses[commands.index(message[2:])]
        else:
            return 'Command not found'
    else:
        if message.lower() in greetings:
            return random.choice(greetings)
        elif message.lower() in hypes or message.lower() == 'w':
            return random.choice(hypes)
        elif message.lower() in trolls or message.lower() == 'l':
            return random.choice(trolls)
        elif message.lower() in ratios or message.lower() == 'l':
            return random.choice(ratios)
        elif message.lower() == 'le':
            return random.choice(gm)
