#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/20 19:01
# @Author: Aaron Meng
# @File  : 37solveSudoku.py
from typing import List


class Solution:
    @staticmethod
    def solveSudoku(board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution.solveSudoku(board))
