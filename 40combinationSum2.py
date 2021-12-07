#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/26 11:05
# @Author: Aaron Meng
# @File  : 40combinationSum2.py
from typing import List


class Solution:
    @staticmethod
    def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        path = []

        def backtracking(start=0):
            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(start, n):
                if sum(path) + candidates[i] > target: return
                if i > start and candidates[i] == candidates[i - 1]: continue
                path.append(candidates[i])
                backtracking(i + 1)
                path.pop()

        backtracking()
        return res


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution.combinationSum2(candidates, target))
