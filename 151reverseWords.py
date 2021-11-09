#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/17 9:59
# @Author: Aaron Meng
# @File  : 151reverseWords.py
from typing import List


class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        return ' '.join(reversed(s.split()))

    @staticmethod
    def reverseWords2(s: str) -> str:
        pass



if __name__ == '__main__':
    s = "the sky is blue"
    print(Solution.reverseWords(s))
