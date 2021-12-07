#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/26 11:36
# @Author: Aaron Meng
# @File  : 216combinationSum3.py
from typing import List


class Solution:
    @staticmethod
    def combinationSum3(k: int, n: int) -> List[List[int]]:
        path = []
        res = []

        def backtracking(kk=k, start=1):
            s = sum(path)
            if s == n:
                res.append(path[:])
                return
            if kk == 0 or (19 - kk) * kk < 2 * (n - s) or (1 + kk) * kk > 2 * (n - s): return
            for i in range(start, 9-kk+2):
                if s + i * kk > n:
                    return
                path.append(i)
                backtracking(kk - 1, i + 1)
                path.pop()

        backtracking()
        return res


if __name__ == '__main__':
    k = 9
    n = 45
    print(Solution.combinationSum3(k, n))
