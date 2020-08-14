# -*- coding: utf-8 -*-
# @Time: 2020/8/14 上午10:37
# @Author: guoq
# @Description: 简单算法构造逻辑练习题


def fibonacci(n=2):
    """
    生成斐波那契数列的前n个数
    :param n: int
    :return: none
    """
    # 首先初始化参数
    n1, n2, i = 1, 0, 0
    # 进行n次计算，并更新参数
    while i < n:
        nn = n1 + n2
        print(nn)
        n1, n2 = n2, nn
        i += 1


def perfect_number(n=1000):
    """
    查找n以内所有完美数
    :param n: int
    :return: none
    """
    for num in range(1, n + 1):
        xs = 0
        for x in range(1, num):
            if num % x == 0:
                xs += x
        if xs == num:
            print(num)


def prime_number(n=100):
    """
    查找n以内所有素数
    :param n: int
    :return: none
    """
    for num in range(2, n + 1):
        r = True
        for x in range(2, num):
            if num % x == 0:
                r = False
                break
        if r:
            print(num)


if __name__ == '__main__':
    # fibonacci(5)
    # perfect_number(10000)
    prime_number(1000)
