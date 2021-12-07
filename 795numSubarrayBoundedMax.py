#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/9 15:02
# @Author: Aaron Meng
# @File  : 795numSubarrayBoundedMax.py
from typing import List


class Solution:
    @staticmethod
    def numSubarrayBoundedMax(nums: List[int], left: int, right: int) -> int:
        def atMostK(K):
            ans = 0
            pre = 0
            for i in range(len(nums)):
                if nums[i] <= K:
                    pre += 1
                else:
                    pre = 0
                ans += pre
            return ans

        return atMostK(right) - atMostK(left - 1)

    @staticmethod
    def numSubarrayBoundedMax2(nums: List[int], left: int, right: int) -> int:
        # 太妙了
        ans = 0
        pre = 0
        j = -1
        for i in range(len(nums)):
            if nums[i] > right:
                j = i
            if nums[i] >= left:
                pre = i - j
            ans += pre
        return ans


if __name__ == '__main__':
    A = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
    L = 32
    R = 69
    print(Solution.numSubarrayBoundedMax2(A, L, R))
