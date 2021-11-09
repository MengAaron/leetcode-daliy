#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/12 14:34
# @Author: Aaron Meng
# @File  : 45jump.py
from typing import List
from queue import Queue


class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        "BFS, So Slow"
        q = Queue()
        Set = set()
        n = len(nums)
        q.put((0, nums[0], 0))
        while q:
            cur_index, cur_num, cur_path = q.get()
            if cur_index == n - 1:
                return cur_path
            if cur_index not in Set:
                Set.add(cur_index)
                for next_index in range(cur_index + 1, min(cur_index + cur_num + 1, n)):
                    if next_index not in Set:
                        q.put((next_index, nums[next_index], cur_path + 1))
        return 0

    @staticmethod
    def jump2(nums: List[int]) -> int:
        n = len(nums)
        steps = [0 for _ in range(n)]
        Max = 0
        for i in range(n):
            if i + nums[i] > Max:
                for j in range(Max + 1, min(i + nums[i] + 1, n)):
                    steps[j] = steps[i] + 1
                Max = i + nums[i]
        return steps[-1]

    @staticmethod
    def jump3(nums: List[int]) -> int:
        # 优化存储空间
        n = len(nums)
        Max = 0
        step = 0
        end = 0
        for i in range(n - 1):  # 最后一步不用跳
            Max = max(Max, i + nums[i])
            if i == end:
                end = Max  # 下一跳的最远距离
                step += 1

        return step


if __name__ == '__main__':
    nums = [2, 1, 1, 4, 5]
    print(Solution.jump3(nums))
