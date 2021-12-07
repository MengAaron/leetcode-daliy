#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/29 12:22
# @Author: Aaron Meng
# @File  : 131partition.py
from typing import List


class Solution:
    @staticmethod
    def partition(s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = f[i + 1][j - 1] and (s[i] == s[j])

        def backtracking(start=0):
            if start == n:
                res.append(path[:])
                return
            for i in range(start, n):
                ans = s[start:i + 1]
                if f[start][i]:
                    path.append(ans)
                    backtracking(i+1)
                    path.pop()

        backtracking()
        return res


if __name__ == '__main__':
    s = 'aaccaa'
    print(Solution.partition(s))
