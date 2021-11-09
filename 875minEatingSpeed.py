#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/8 19:08
# @Author: Aaron Meng
# @File  : 875minEatingSpeed.py
from typing import List


class Solution:
    @staticmethod
    def minEatingSpeed(piles: List[int], h: int) -> int:
        def Check(v):
            t = 0
            for pile in piles:
                t += (pile - 1) // v + 1
                if t > h:
                    return False
            return True

        sump, maxp, n = sum(piles), max(piles), len(piles)
        if n == h: return maxp
        left, right = (sump - 1) // h + 1, min(maxp, sump // (h - n))
        while left < right:
            mid = left + (right - left) // 2
            if Check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    piles = [30, 11, 23, 4, 20]
    H = 5
    print(Solution.minEatingSpeed(piles, H))
