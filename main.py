from commands import load
from commander import Commander


def main():
    load()
    commander = Commander()
    commander.command_yield()


if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
