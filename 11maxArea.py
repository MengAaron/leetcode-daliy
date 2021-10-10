#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/10 17:29
# @Author: Aaron Meng
# @File  : 11maxArea.py
from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxArea = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                i += 1
                maxArea = max(maxArea, (j - i) * min(height[i], height[j]))
            else:
                j -= 1
                maxArea = max(maxArea, (j - i) * min(height[i], height[j]))
        return maxArea


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution.maxArea(height))
