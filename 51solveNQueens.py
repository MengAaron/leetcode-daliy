#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/8 20:11
# @Author: Aaron Meng
# @File  : 51solveNQueens.py
from typing import List


class Solution:
    @staticmethod
    def solveNQueens(n: int) -> List[List[str]]:
        ans = []
        path = []
        valid_set = set(range(n))

        def backtracking(depth=0):
            if depth == n:
                ans.append(['.' * k + 'Q' + '.' * (n - k - 1) for k in path])
                return

            for i in valid_set.copy():
                flag = 0
                if depth > 0:
                    temp_row, temp_col = depth, i
                    for row, col in enumerate(path):
                        if temp_row - row == abs(temp_col - col):
                            flag = 1
                            break
                if flag:
                    continue
                valid_set.remove(i)
                path.append(i)
                backtracking(depth+1)
                valid_set.add(i)
                path.pop()

        backtracking()
        return ans


if __name__ == '__main__':
    n = 8
    print(Solution.solveNQueens(n))
