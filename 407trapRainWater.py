#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/16 11:40
# @Author: Aaron Meng
# @File  : 407trapRainWater.py
from typing import List


class Solution:
    @staticmethod
    def trapRainWater(heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])


if __name__ == '__main__':
    heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    print(Solution.trapRainWater(heightMap))
