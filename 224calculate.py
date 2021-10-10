#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/7 10:56
# @Author: Aaron Meng
# @File  : calculate.py
from typing import List




class Solution:
    @staticmethod
    def calculate(s: str) -> int:
        stack = []
        buffer = 0
        for char in s:
            if char == '(':
                stack.append(buffer)
            elif char == ')':



if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    print(Solution.calculate(s))
