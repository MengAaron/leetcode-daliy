#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/4 22:52
# @Author: Aaron Meng
# @File  : 90subsetsWithDup.py
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def subsetsWithDup(nums: List[int]) -> List[List[int]]:
        res = [[]]
        cnt = Counter(nums)
        for k, v in cnt.items():
            for i in range(len(res)):
                res.extend([res[i] + [k] * (j + 1) for j in range(v)])
        return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    print(Solution.subsetsWithDup(nums))
