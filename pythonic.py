#!/usr/bin/env python3


def test_with():
    # pythonic 写法
    with open('pythonic.py', encoding='utf-8') as fp:
        for line in fp:
            print(line[:-1])

    # 一般写法
    fp = open('pythonic.py', encoding='utf-8')
    for line in fp:
        print(line[:-1])
    fp.close()


def test_else():
    # pythonic 写法
    for cc in ['UK', 'ID', 'JP', 'US']:
        if cc == 'CN':
            break
    else:
        print('no CN')

    # 一般写法
    no_cn = True
    for cc in ['UK', 'ID', 'JP', 'US']:
        if cc == 'CN':
            no_cn = False
            break
    if no_cn:
        print('no CN')


def test_list():
    # pythonic 写法
    squares = [x * x for x in range(10)]
    print(squares)

    # 一般写法
    squares = []
    for x in range(10):
        squares.append(x * x)
    print(squares)


def test_map():
    m = {'one': 1, 'two': 2, 'three': 3}
    for k, v in m.items():
        print(k, v)

    for k, v in sorted(m.items()):
        print(k, v)


def test_yield():
    def fibonacci():
        num0 = 0
        num1 = 1
        for _ in range(10):
            num2 = num0 + num1
            yield num2
            num0 = num1
            num1 = num2

    for i in fibonacci():
        print(i)


def main():
    test_with()
    test_else()
    test_list()
    test_map()
    test_yield()


if __name__ == '__main__':
    main()
