"""A local educational assistant with explicit, limited commands."""
from datetime import datetime
import webbrowser

DOCUMENTATION_URL = 'https://docs.github.com/'


def respond(command, ask=input, say=print, open_url=webbrowser.open):
    command = command.strip().casefold()
    if command == 'help':
        say('Commands: help, time, open github documentation, quit')
    elif command == 'time':
        say(datetime.now().astimezone().strftime('%H:%M %Z'))
    elif command == 'open github documentation':
        if ask('Open GitHub documentation in your browser? [y/N] ').strip().casefold() == 'y':
            open_url(DOCUMENTATION_URL)
            say('Requested documentation in your browser.')
        else:
            say('Cancelled.')
    elif command == 'quit':
        say('Goodbye.')
        return False
    else:
        say('Unknown command. Type help.')
    return True


def main():
    print('Jarvis educational starter. Type help or quit.')
    try:
        while respond(input('You: ')):
            pass
    except (EOFError, KeyboardInterrupt):
        print('\nGoodbye.')


if __name__ == '__main__':
    main()
