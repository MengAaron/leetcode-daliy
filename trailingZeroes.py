#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/26 9:47
# @Author: Aaron Meng
# @File  : trailingZeroes.py

class Solution:
    @staticmethod
    def trailingZeroes(n: int) -> int:
        # 递归方法
        if n < 5:
            return 0
        five_number = 0
        temp = n
        while not temp % 5:
            temp //= 5
            five_number += 1
        return five_number + Solution.trailingZeroes(n - 1)

    @staticmethod
    def trailingZeroes2(n: int) -> int:
        # 数存在5因子的个数，下次就数n//5里面存在5因子个数（相当于n里存在25因子个数）
        res = 0
        while n >= 4:
            n //= 5
            res += n
        return res


def factorial(n: int):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 99
    print(factorial(n))
    print(Solution.trailingZeroes(n))
    print(Solution.trailingZeroes2(n))
