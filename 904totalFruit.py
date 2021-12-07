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

    @staticmethod
    def totalFruit2(fruits: List[int]) -> int:
        n = len(fruits)
        m = {}
        ans = j = cnt = 0
        for i in range(n):
            if fruits[i] not in m:
                cnt += 1
            m[fruits[i]] = i
            while j < n and cnt > 2:
                if m[fruits[j]] == j:
                    m.pop(fruits[j])
                    cnt -= 1
                j += 1
            if cnt <= 2:
                ans = max(i - j + 1, ans)
        return ans




if __name__ == '__main__':
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print(Solution.totalFruit(fruits))
