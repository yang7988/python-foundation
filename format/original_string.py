# r或者R开头的字符串为原始字符串，即使遇到转义字符也原样展示并不会真的的转义
# 在处理正则表达式时应全程使用原始字符串。否则，将会有大量 Backwhacking 需要处理

def format_row_str():
    str = r"Newlines are indicated by \n"
    print(str)


if __name__ == '__main__':
    format_row_str()
