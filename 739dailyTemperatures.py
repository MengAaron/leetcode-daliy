#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/19 16:42
# @Author: Aaron Meng
# @File  : dailyTemperatures.py
from typing import List


class Solution:
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        # 单调递减栈（下一步尝试倒着来，用递增栈）
        index_stack, res = [], [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while len(index_stack) != 0 and temperatures[index_stack[-1]] < temp:
                prev_index = index_stack.pop()
                res[prev_index] = i - prev_index
            index_stack.append(i)
        return res

    @staticmethod
    def dailyTemperatures2(temperatures: List[int]) -> List[int]:
        index_stack, res = [], [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while len(index_stack) != 0 and temperatures[index_stack[-1]] <= temperatures[i]:
                index_stack.pop()
            if index_stack:
                res[i] = index_stack[-1] - i
            index_stack.append(i)
        return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution.dailyTemperatures2(temperatures))
