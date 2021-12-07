#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/22 20:23
# @Author: Aaron Meng
# @File  : 17letterCombinations.py
from typing import List


class Solution:
    @staticmethod
    def letterCombinations(digits: str) -> List[str]:
        if not digits:
            return list()
        n = len(digits)
        path = []
        res = []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtracking(start):
            if len(path) == n:
                res.append(''.join(path))
                return
            for char in phoneMap[digits[start]]:
                path.append(char)
                backtracking(start+1)
                path.pop()
        backtracking(0)
        return res


if __name__ == '__main__':
    digits = "234"
    print(Solution.letterCombinations(digits))
