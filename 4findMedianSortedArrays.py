#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/15 21:42
# @Author: Aaron Meng
# @File  : 4findMedianSortedArrays.py
from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        infinity = 10 ** 6 + 1

        def findKthElement(i, j, k):
            if i >= m: return nums2[j + k - 1]
            if j >= n: return nums1[i + k - 1]
            if (k == 1): return min(nums1[i], nums2[j])
            midVal1 = nums1[i + k // 2 - 1] if i + k // 2 <= m else infinity
            midVal2 = nums2[j + k // 2 - 1] if j + k // 2 <= n else infinity
            return findKthElement(i + k // 2, j, k - k // 2) if midVal1 < midVal2 else findKthElement(i, j + k // 2,
                                                                                                      k - k // 2)

        return (findKthElement(0, 0, (m + n + 1) // 2) + findKthElement(0, 0, (m + n + 2) // 2)) / 2

    @staticmethod
    def findMedianSortedArrays2(nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        infinity = 10 ** 6 + 1
        def findKthElement(k):
            i, j = 0, 0
            while True:
                if i >= m: return nums2[j + k - 1]
                if j >= n: return nums1[i + k - 1]
                if (k == 1): return min(nums1[i], nums2[j])
                midVal1 = nums1[i + k // 2 - 1] if i + k // 2 <= m else infinity
                midVal2 = nums2[j + k // 2 - 1] if j + k // 2 <= n else infinity
                if midVal1 < midVal2:
                    i += k // 2
                else:
                    j += k // 2
                k -= k // 2

        return (findKthElement((m + n + 1) // 2) + findKthElement((m + n + 2) // 2)) / 2


if __name__ == '__main__':
    nums1 = [0, 0]
    nums2 = [0, 0]
    print(Solution.findMedianSortedArrays2(nums1, nums2))
