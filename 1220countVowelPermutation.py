#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/1/17 19:18
# @Author: Aaron Meng
# @File  : 1220countVowelPermutation.py
from typing import List, Optional


class Solution:
    @staticmethod
    def countVowelPermutation(n: int) -> int:
        # dic = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        # lst = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        # matrix = [[1]*5] + [[0]*5 for _ in range(n-1)]
        # for i in range(1,n):
        #     for j in range(5):
        #         for k in lst[j]:
        #             matrix[i][j] += matrix[i-1][k]
        # ans = sum(matrix[-1])
        # return ans % (10 ** 9 + 7)
        a, e, i, o, u, M = 1, 1, 1, 1, 1, 10 ** 9 + 7
        for _ in range(n - 1):
            a, e, i, o, u = (e + u + i) % M, (a + i) % M, (e + o) % M, i % M, (o + i) % M
        return sum([a, e, i, o, u]) % M


if __name__ == '__main__':
    print(Solution.countVowelPermutation(5))
