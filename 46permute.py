#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/4 23:21
# @Author: Aaron Meng
# @File  : 46permute.py
from typing import List


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtracking(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtracking(nums, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution.permute(nums))
