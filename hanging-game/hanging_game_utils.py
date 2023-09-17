# Utility functions for the game

def print_welcome_message():
    message = "Welcome to Python Hanging Game!\nGuessing topic will be about PC Hardware. Good luck!"
    message_lines = message.split("\n")
    max_line_length = max(len(line) for line in message_lines) # generator expression
    border = '+' + '-' * (max_line_length + 2) + '+'

    print(border)
    for line in message_lines:
        print(f'| {line.center(max_line_length)} |')
    print(border)
