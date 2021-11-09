#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/11 20:24
# @Author: Aaron Meng
# @File  : 55canJump.py
from typing import List


class Solution:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        "DFS, So Slow"
        stack = []
        Set = set()
        n = len(nums)
        stack.append((0, nums[0]))
        while stack:
            cur_index, cur_num = stack.pop()
            if cur_index == n - 1:
                return True
            if cur_index not in Set:
                Set.add(cur_index)
                for next_index in range(cur_index + 1, min(cur_index + cur_num + 1, n)):
                    if next_index not in Set:
                        stack.append((next_index, nums[next_index]))
        return False

    @staticmethod
    def canJump2(nums: List[int]) -> bool:
        "Greedy Search"
        n, most = len(nums), 0
        for i in range(n):
            if i > most:
                return False
            most = max(most, i + nums[i])
            if most >= n - 1:
                return True
        return False


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    print(Solution.canJump2(nums))
