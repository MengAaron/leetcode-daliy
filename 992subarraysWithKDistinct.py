#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/9 17:33
# @Author: Aaron Meng
# @File  : 992subarraysWithKDistinct.py
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def subarraysWithKDistinct(nums: List[int], k: int) -> int:
        def atMostK(k):
            counter = Counter()
            res = i = 0
            for j in range(len(nums)):
                if counter[nums[j]] == 0:
                    k -= 1
                counter[nums[j]] += 1
                while k < 0:
                    counter[nums[i]] -= 1
                    if counter[nums[i]] == 0:
                        k += 1
                    i += 1
                res += j - i + 1
            return res

        return atMostK(k) - atMostK(k - 1)

    @staticmethod
    def subarraysWithKDistinct2(nums: List[int], k: int) -> int:
        m = {}
        n = len(nums)
        cnt = j = ans = 0
        for i in range(n):
            if nums[i] not in m:
                cnt += 1
            m[nums[i]] = i
            while j<n and cnt == k+1:
                if m[nums[j]] == j:
                    m.pop(nums[j])
                j += 1
                cnt -= 1
            if cnt == k:
                tj = j
                while m[nums[tj]] != tj:
                    tj += 1
                ans += tj - j + 1
        return ans


if __name__ == '__main__':
    A = [1, 2, 1, 3, 4]
    K = 3
    print(Solution.subarraysWithKDistinct(A, K))
