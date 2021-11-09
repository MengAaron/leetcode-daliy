#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/25 15:39
# @Author: Aaron Meng
# @File  : 740deleteAndEarn.py
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def deleteAndEarn(nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        n = len(counter.keys())
        if n == 0:
            return 0
        if n == 1:
            return nums[0] * counter[nums[0]]

        dp, dp0, last_key = 0, 0, -1
        for key, value in counter.items():
            temp = dp0
            dp0 = dp
            if key == last_key + 1:
                dp = max(dp, temp + key * value)
            else:
                dp = dp + key * value
            last_key = key
        return dp


if __name__ == '__main__':
    nums = [3, 1]
    print(Solution.deleteAndEarn(nums))
