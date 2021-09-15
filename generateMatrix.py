#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/10 19:12
# @Author: Aaron Meng
# @File  : generateMatrix.py
from typing import List


class Solution:
    @staticmethod
    def generateMatrix(n: int) -> List[List[int]]:
        ans = [[0 for j in range(n)] for i in range(n)]
        left, right, up, down = 0, n, 0,n
        i,j,k = 0,0,1
        while True:
            if up >= down:
                break
            for j in range(left, right):
                ans[i][j] = k
                k += 1
            up += 1
            if left >= right:
                break
            for i in range(up, down):
                ans[i][j] = k
                k += 1
            right -= 1
            if up >= down:
                break
            for j in range(right - 1, left - 1, -1):
                ans[i][j] = k
                k += 1
            down -= 1
            if left >= right:
                break
            for i in range(down - 1, up - 1, -1):
                ans[i][j] = k
                k += 1
            left += 1
        return ans


if __name__ == '__main__':
    n = 10
    matrix = Solution.generateMatrix(n)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

