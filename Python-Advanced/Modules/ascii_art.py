from pyfiglet import figlet_format


def print_art(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)


text = input()
print_art(text)
