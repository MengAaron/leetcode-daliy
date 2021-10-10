#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/7 10:06
# @Author: Aaron Meng
# @File  : trapRainWater.py
from typing import List


class Solution:
    @staticmethod
    def trapRainWater(height: List[int]) -> int:
        rainWater = 0
        stack = []
        for i, h in enumerate(height):
            while stack and h > stack[-1][1]:
                _, cur_height = stack.pop()
                rainWater += (min(h, stack[-1][1]) - cur_height) * (i - stack[-1][0] - 1) if stack else 0
            stack.append((i,h))
        return rainWater


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution.trapRainWater(height))
