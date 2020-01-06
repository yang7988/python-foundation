def format_end():
    print('a', end='')
    print('b', end='')


def format_placeholder_end():
    print('{name} wrote {book}'.format(name="Swaroop'", book="A Byte of Python"), end=" end")


if __name__ == '__main__':
    format_end()
    format_placeholder_end()

