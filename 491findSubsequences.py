#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/5 19:49
# @Author: Aaron Meng
# @File  : 491findSubsequences.py
from typing import List


class Solution:
    @staticmethod
    def findSubsequences(nums: List[int]) -> List[List[int]]:
        """
        该方法不需要考虑去重问题，通过累加小于等于当前num的list，每次suffix[num]都会更新
        :param nums:
        :return:
        """
        res = []
        suffix = {}
        for num in nums:
            new = [[num]]
            for sfx in suffix:
                if sfx <= num:
                    new += [_ + [num] for _ in suffix[sfx]]
            suffix[num] = new
        for sfx in suffix:
            for i in range(1, len(suffix[sfx])):
                res.append(suffix[sfx][i])
        return res


if __name__ == '__main__':
    nums = [4, 7, 6, 7]
    print(Solution.findSubsequences(nums))
