# -*- coding: utf-8 -*-
# @Time: 2020/8/14 下午3:33
# @Author: guoq
# @Description: 练习字符串和常用的数据结构
import os
import time
import random


def horse_race():
    """
    输入文字跑马灯
    :return:
    """
    content = input('请输入跑马灯内容：')
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


def gen_code(num):
    """
    随机生成指定长度的验证码
    :param num: int
    :return: string
    """
    code = ''
    source = '12345367890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(num):
        index = random.randint(0, len(source) - 1)
        code += source[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    返回输入文件名的后缀
    :param filename: string 输入文件名
    :param has_dot: bool 输出是否带.
    :return: string
    """
    dot_index = 0
    for i, s in enumerate(filename[::-1]):
        if s == '.':
            dot_index = i
            break
    dot_index = len(filename) - dot_index
    return '.' + filename[dot_index:] if has_dot else filename[dot_index:]


def max2(nums):
    """
    返回输入列表中最大和第二大的值
    :param nums: list
    :return:
    """
    # 首先选出前两个值按大小排列
    (m1, m2) = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
    # 遍历剩下的值，对结果进行更新
    for i in range(2, len(nums)):
        if nums[i] > m1:
            m2 = m1
            m1 = nums[i]
        elif nums[i] > m2:
            m2 = nums[i]
    return m1, m2


def joseph_circle(num):
    """
    约瑟夫环
    :param num: int
    :return: list
    """
    # 生成每个人的初始化状态
    person = [True] * num
    # 生成需报数的索引，更新每个人的状态
    indexes = range(person)



if __name__ == '__main__':
    # horse_race()
    # code = gen_code(6)
    # filename = 'lksdfk/sdlf;s/sdfasdf/sdfasv/sajdlastxt'
    # suffix = get_suffix(filename)
    nums = [1, 23, 34, 226, 31]
    m1, m2 = max2(nums)
    print('%d %d' % (m1, m2))
