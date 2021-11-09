#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/25 15:03
# @Author: Aaron Meng
# @File  : 213rob2.py
from typing import List


class Solution:
    @staticmethod
    def rob2(nums: List[int]) -> int:
        def rob(nums: List[int]) -> int:
            n = len(nums)
            if n == 1:
                return nums[0]
            dp0 = nums[0]
            dp1 = max(nums[0], nums[1])
            for i in range(2, n):
                dp = max(dp1, dp0 + nums[i])
                dp0 = dp1
                dp1 = dp
            return dp1

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(rob(nums[:-1]), rob(nums[1:]))


if __name__ == '__main__':
    nums = [1]
    print(Solution.rob2(nums))
