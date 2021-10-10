#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/6 10:53
# @Author: Aaron Meng
# @File  : largestRectangleArea.py
from typing import List

class Solution:
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        if not heights:
            return 0
        mono_stack = []
        max_area = 0
        heights.append(0)
        for i, height in enumerate(heights):
            while mono_stack and mono_stack[-1][1] > heights[i]:
                _, cur_height = mono_stack.pop()
                last_index = mono_stack[-1][0] + 1 if mono_stack else 0
                cur_area = (i - last_index) * cur_height
                max_area = cur_area if cur_area > max_area else max_area
            mono_stack.append((i, height))
        return max_area



if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    print(Solution.largestRectangleArea(heights))
