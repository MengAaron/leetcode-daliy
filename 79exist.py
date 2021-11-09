#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/1 14:23
# @Author: Aaron Meng
# @File  : 79exist.py
from typing import List


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check(i, j, visited, word):
            if board[i][j] == word:
                return True

            if board[i][j] == word[0]:
                visited[i][j] = 1
                for direction in directions:
                    cur_i = i + direction[0]
                    cur_j = j + direction[1]
                    if cur_i >= 0 and cur_i < m and cur_j >= 0 and cur_j < n and visited[cur_i][cur_j] == 0:
                        if check(cur_i, cur_j, visited, word[1:]):
                            return True
                visited[i][j] = 0
            else:
                return False

        for i in range(m):
            for j in range(n):
                if check(i, j, visited, word):
                    return True
        return False


if __name__ == '__main__':
    board = [["a"]]
    word = "a"
    print(Solution.exist(board, word))
