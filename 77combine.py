#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/22 14:04
# @Author: Aaron Meng
# @File  : 77combine.py
from typing import List


class Solution:
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtracking(start):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1 - (k - len(path)) + 1):
                path.append(i)
                backtracking(i + 1)
                path.pop()

        backtracking(1)
        return res


if __name__ == '__main__':
    n = 5
    k = 3
    print(Solution.combine(n, k))
