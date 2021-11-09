#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/25 10:21
# @Author: Aaron Meng
# @File  : 198rob.py
from typing import List


class Solution:
    @staticmethod
    def rob(nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]

    @staticmethod
    def rob2(nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])
        for i in range(2, n):
            dp = max(dp1, dp0 + nums[i])
            dp0 = dp1
            dp1 = dp
        return dp1

if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    print(Solution.rob2(nums))
