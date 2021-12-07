#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/23 9:59
# @Author: Aaron Meng
# @File  : 39combinationSum.py
from typing import List


class Solution:
    @staticmethod
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        path = []
        def backtracking(start):
            if sum(path) == target:
                res.append(path[:])
            for i in range(start, n):
                if candidates[i] + sum(path) > target:
                    break
                path.append(candidates[i])
                backtracking(i)
                path.pop()

        backtracking(0)
        return res



if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    print(Solution.combinationSum(candidates,target))
