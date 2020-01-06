# continue 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭代。
def for_continue():
    while True:
        s = input('Enter something : ')
        if s == 'quit':
            break
        if len(s) < 3:
            print('Too small')
        continue
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理


if __name__ == '__main__':
    for_continue()
