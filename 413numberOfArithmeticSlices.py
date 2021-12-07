#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/23 10:44
# @Author: Aaron Meng
# @File  : 413numberOfArithmeticSlices.py
from typing import List


class Solution:
    @staticmethod
    def numberOfArithmeticSlices(nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        diff = nums[1] - nums[0]
        res = prev = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                prev += 1
                res += prev
            else:
                prev = 0
            diff = nums[i] - nums[i - 1]
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 3, 4, 5, 6, 7]
    print(Solution.numberOfArithmeticSlices(nums))
