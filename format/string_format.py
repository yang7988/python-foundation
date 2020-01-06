def format_string():
    age = 20
    name = "Swaroop"
    print('{0} was {1} years old when he wrote this book'.format(name, age))
    print('Why is {0} playing with that python?'.format(name))


def format_string1():
    age = 20
    name = "Swaroop"
    print('{} was {} years old when he wrote this book'.format(name, age))
    print('Why is {} playing with that python?'.format(name))


if __name__ == '__main__':
    format_string()
    format_string1()
