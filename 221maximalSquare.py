#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/8 10:00
# @Author: Aaron Meng
# @File  : 221maximalSquare.py
from typing import List


class Solution:
    @staticmethod
    def maximalSquare(matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 if matrix[i][j] == '1' else 0
        return max(dp[i][j] for j in range(n) for i in range(m)) ** 2


if __name__ == '__main__':
    # matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
    #           ["1", "0", "0", "1", "0"]]
    matrix = [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"],
              ["0", "1", "1", "1"]]
    print(Solution.maximalSquare(matrix))
