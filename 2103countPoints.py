#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/12 10:35
# @Author: Aaron Meng
# @File  : 5952countPoints.py
from typing import List
from collections import Counter,defaultdict


class Solution:
    @staticmethod
    def countPoints(rings: str) -> int:
        cnt = defaultdict(Counter)
        n = len(rings) // 2
        res = 0
        for i in range(n):
            cnt[rings[2*i+1]][rings[2*i]] += 1
        for _ in cnt.copy():
            if len(cnt[_]) == 3:
                res += 1
        return res


if __name__ == '__main__':
    rings = "B0B6G0R6R0R6G9"
    print(Solution.countPoints(rings))
