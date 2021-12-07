#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/3 17:30
# @Author: Aaron Meng
# @File  : 78subsets.py
from typing import List


class Solution:
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        res = [[]]
        path = []
        n = len(nums)
        def backtracking(start=0):
            for i in range(start,n):
                path.append(nums[i])
                res.append(path[:])
                backtracking(i+1)
                path.pop()
        backtracking()
        return res

    def subsets2(nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution.subsets2(nums))
