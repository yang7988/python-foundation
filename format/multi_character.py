# 定义多行字符串"""
def format_multi_character():
    str = """
        this is first line
        this is second line
        this is spec line \n aa
    """
    print(str)


# \n换行符
def format_newline():
    print('This is the first line\nThis is the second line')

# 末尾的\将在下一行继续
def special_escape():
    str = "This is the first sentence. \
          This is the second sentence."
    print(str)


if __name__ == '__main__':
    format_multi_character()
    format_newline()
    special_escape()
