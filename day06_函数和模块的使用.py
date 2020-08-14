# -*- coding: utf-8 -*-
# @Time: 2020/8/14 上午11:41
# @Author: guoq
# @Description: 练习函数和模块


def gcd(x, y):
    """
    求两个自然数的最大公约数
    :param x: int
    :param y: int
    :return: int
    """
    (x, y) = (y, x) if y > x else (x, y)
    for num in range(x, 0, -1):
        if x % num == 0 and y % num == 0:
            return num


def lcm(x, y):
    """
    求两个自然数的最小公倍数
    :param x: int
    :param y: int
    :return: int
    """
    return x * y // gcd(x, y)


def is_palindrome(num):
    """
    判断一个数是不是回文数
    :param num: int
    :return: bool
    """
    # 初始化参数
    tmp = num
    reverse = 0
    # 将输入的数字反转,并更新参数
    while tmp > 0:
        reverse = reverse * 10 + tmp % 10
        tmp //= 10
    return reverse == num


def is_prime(num):
    """
    判断一个数是不是素数
    :param num: int
    :return:  bool
    """
    is_true = True
    for x in range(2, num):
        if num % x == 0:
            is_true = False
            break
    return is_true if num != 1 else False


def is_palindrome_and_prime():
    while True:
        num = int(input("请输入一个正整数"))
        if is_prime(num) and is_palindrome(num):
            print('%d 是一个回文素数' % num)
        else:
            print('%d 不是一个回文素数' % num)


if __name__ == '__main__':
    # g = gcd(128, 1024)
    # l = lcm(1024, 128)
    # i = is_palindrome(12321)
    # is_p = is_prime(2)
    # print(is_p)
    is_palindrome_and_prime()
