#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/21 9:56
# @Author: Aaron Meng
# @File  : 1047removeDuplicates.py
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(s: str) -> str:
        stack = ['InValid']
        for char in s:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack[1:])


if __name__ == '__main__':
    s = "abbaca"
    print(Solution.removeDuplicates(s))
