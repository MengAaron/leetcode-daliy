#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/4 23:22
# @Author: Aaron Meng
# @File  : 47permuteUnique.py
from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def permuteUnique(nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        ans = []

        def backtracking(cnt, tmp):
            if not cnt:
                ans.append(tmp)
                return
            for k in cnt.copy():
                cnt[k] -= 1
                if cnt[k] == 0:
                    cnt.pop(k)
                backtracking(cnt, tmp + [k])
                cnt[k] += 1

        backtracking(cnt, [])
        return ans


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3]
    print(Solution.permuteUnique(nums))
