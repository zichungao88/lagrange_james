import random
import json


def respond(msg: str) -> str:
    message = msg.lower()

    with open('commands.json', 'r') as command:
        command_data = json.load(command)
        commands = command_data['commands']

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

    with open('le.txt', 'r') as gm:
        le = gm.read().split('\n')
        le.pop()

    with open('players.txt', 'r') as player:
        players = player.read().split('\n')
        players.pop()

    with open('entities.txt', 'r') as entity:
        entities = entity.read().split('\n')
        entities.pop()

    if message[:2] == '//':
        command = message[2:]
        if command in commands:
            if commands[command] == '__HELP__':
                help_msg = '```List of all commands (prefix: //)\n(Note: all commands are case sensitive (lowercase only))\n\n'
                sorted_commands = ['help'] + sorted(cmd for cmd in commands.keys() if cmd != 'help')
                help_msg += '\n'.join(f'{cmd} {'(shows this message)' if cmd == 'help' else ''}' for cmd in sorted_commands)
                help_msg += '```'
                return help_msg
            return commands[command]
        else:
            return 'Invalid command'
    else:
        if message.lower() in greetings:
            return random.choice(greetings)
        elif message.lower() in hypes or message.lower() == 'w':
            return random.choice(hypes)
        elif message.lower() in trolls or message.lower() == 'l':
            return random.choice(trolls)
        elif message.lower() in ratios or message.lower() == 'l':
            return random.choice(ratios)
        elif message.lower() == '.':
            return random.choice(le)
        elif message.lower() == 'who':
            return random.choice(players)
        elif message.lower() == 'what':
            return random.choice(entities)
        return ''
