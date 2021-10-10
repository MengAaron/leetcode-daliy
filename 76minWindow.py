#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/9 9:47
# @Author: Aaron Meng
# @File  : minWindow.py
from typing import List
import collections


class Solution:
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        t_counter = collections.Counter(t)
        res = (0, float("inf"))
        need = len(t)
        left = 0   # start
        for right,c in enumerate(s):    # end
            if c in t_counter:
                if t_counter[c]>0:
                    need -= 1
                t_counter[c] -= 1
                while need == 0:
                    if s[left] in t_counter:
                        if t_counter[s[left]] == 0:
                            need += 1
                            if right - left + 1 < res[1] - res[0] + 1:
                                res = (left, right)
                        t_counter[s[left]] += 1
                    left += 1
        return "" if res[1] == float("inf") else s[res[0]:res[1] + 1]



if __name__ == '__main__':
    s = "AAC"
    t = "ABC"
    print(Solution.minWindow(s, t))
