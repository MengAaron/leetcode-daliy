#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/7 19:33
# @Author: Aaron Meng
# @File  : totalFruit.py
from typing import List


class Solution:
    @staticmethod
    def totalFruit(fruits: List[int]) -> int:
        # j,k = 0, 0
        n = len(fruits)
        start, ans = 0, 0
        while start < n:
            endJ, endK, fruitJ, fruitK, tempans = start, -1, fruits[start], -1, 1
            for i in range(start + 1, n):
                if fruits[i] == fruitJ:
                    endJ = i
                    tempans += 1
                    continue
                elif fruitK < 0:
                    endK = i
                    fruitK = fruits[i]
                    tempans += 1
                elif fruits[i] == fruitK:
                    endK = i
                    tempans += 1
                    continue
                else:
                    break
            if tempans > ans:
                ans = tempans
            if endK < 0:
                break
            start = endJ + 1 if endJ < endK else endK + 1
        return ans


if __name__ == '__main__':
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    print(Solution.totalFruit(fruits))
