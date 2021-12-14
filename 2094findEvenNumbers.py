#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/10 9:51
# @Author: Aaron Meng
# @File  : 2094findEvenNumbers.py
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def findEvenNumbers(digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ans = []
        def backtracking(depth=0,path=0):
            if depth == 3:
                if path % 2 == 0:
                    ans.append(path)
                return
            for i in cnt.copy():
                if depth == 0 and i == 0:
                    continue
                cnt[i] -= 1
                if not cnt[i]:
                    cnt.pop(i)
                backtracking(depth+1,10*path + i)
                cnt[i] += 1
        backtracking()
        ans.sort()
        return ans




if __name__ == '__main__':
    digits = [2, 2, 8, 8, 2]
    print(Solution.findEvenNumbers(digits))
