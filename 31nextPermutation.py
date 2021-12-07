#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/20 19:10
# @Author: Aaron Meng
# @File  : 31nextPermutation.py
from typing import List


class Solution:
    @staticmethod
    def nextPermutation(nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [1, 5, 1]
    print(Solution.nextPermutation(nums))
