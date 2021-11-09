#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/21 10:05
# @Author: Aaron Meng
# @File  : 20isValid.py
from typing import List


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack = ['?']
        char_dict = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif char_dict[c] != stack.pop():
                return False
        return len(stack) == 1


if __name__ == '__main__':
    s = "{[]}"
    print(Solution.isValid(s))
