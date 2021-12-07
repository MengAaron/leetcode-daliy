#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/7 10:06
# @Author: Aaron Meng
# @File  : trapRainWater.py
from typing import List


class Solution:
    @staticmethod
    def trapRainWater(height: List[int]) -> int:
        # 对于每个柱子，找两边的最大高度，一个柱子对应一个面积
        rainWater = 0
        stack = []
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom_idx = stack.pop()
                while stack and height[bottom_idx] == height[stack[-1]]:
                    stack.pop()
                if stack:
                    curHeight = min(h, height[stack[-1]]) - height[bottom_idx]
                    curWidth = i - stack[-1] - 1
                    rainWater += curHeight * curWidth
            stack.append(i)
        return rainWater

    @staticmethod
    def trapRainWater2(height: List[int]) -> int:
        n = len(height)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = height[0]
        dp[-1][1] = height[-1]
        res = 0
        for i in range(1, n):
            dp[i][0] = max(height[i], dp[i - 1][0])
        for j in range(n - 2, -1, -1):
            dp[j][1] = max(height[j], dp[j + 1][1])
        for i in range(1, n - 1):
            res += min(dp[i]) - height[i]
        return res

    @staticmethod
    def trapRainWater3(height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lmax = rmax = res = 0
        while left <= right:
            if lmax <= rmax:
                lmax = max(lmax, height[left])
                res += lmax - height[left]
                left += 1
            else:
                rmax = max(rmax, height[right])
                res += rmax - height[right]
                right -= 1
        return res


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution.trapRainWater3(height))
