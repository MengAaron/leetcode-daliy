#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/9 23:16
# @Author: Aaron Meng
# @File  : spiralOrder.py
from typing import List


class Solution:
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        left, right, up, down = 0, len(matrix[0]), 0, len(matrix)
        ans = []
        i, j = 0, 0  # row, column
        while True:
            if up >= down:
                break
            for j in range(left, right):
                ans.append(matrix[i][j])
            up += 1
            if left >= right:
                break
            for i in range(up, down):
                ans.append(matrix[i][j])
            right -= 1
            if up >= down:
                break
            for j in range(right - 1, left - 1, -1):
                ans.append(matrix[i][j])
            down -= 1
            if left >= right:
                break
            for i in range(down - 1, up - 1, -1):
                ans.append(matrix[i][j])
            left += 1
        return ans

    @staticmethod
    def spiralOrder2(matrix: List[List[int]]) -> List[int]:
        r, i, j, di, dj = [], 0, 0, 0, 1
        for _ in range(len(matrix) * len(matrix[0])):
            r.append(matrix[i][j])
            matrix[i][j] = 0
            if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
                di, dj = dj, -di
            i += di
            j += dj
        return r


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print(Solution.spiralOrder2(matrix))
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print(Solution.spiralOrder2(matrix))
    matrix = [[2,5,8],[4,0,-1]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print(Solution.spiralOrder2(matrix))
