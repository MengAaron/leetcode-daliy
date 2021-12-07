#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/20 16:10
# @Author: Aaron Meng
# @File  : 470rand10.py
from typing import List
import random


def rand7():
    return random.randint(1, 7)


class Solution:
    @staticmethod
    def rand10():
        while True:
            a = rand7()
            b = rand7()
            res = (a - 1) * 7 + b
            if res <= 40:
                return (res - 1) // 4 + 1
            a = res - 40
            b = rand7()
            res = (a - 1) * 7 + b
            if res <= 60:
                return (res - 1) // 6 + 1
            a = res - 60
            b = rand7()
            res = (a - 1) * 7 + b
            if res <= 20:
                return (res - 1) // 2 + 1


if __name__ == '__main__':
    import collections

    c = collections.Counter()
    for _ in range(10000):
        c[Solution.rand10()] += 1
    print(c)
