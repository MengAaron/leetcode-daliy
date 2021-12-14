  #!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/12 10:42
# @Author: Aaron Meng
# @File  : 5953subArrayRanges.py
from typing import List


class Solution:
    @staticmethod
    def subArrayRanges(nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n - 1):
            maxx, minn = nums[i], nums[i]
            for j in range(i + 1, n):
                if nums[j] > maxx:
                    maxx = nums[j]
                elif nums[j] < minn:
                    minn = nums[j]
                res += maxx - minn
        return res

    def subArrayRanges2(nums: List[int]) -> int:
        # 单调栈，找某个数作为最大/最小值的区间,左闭右开区间，也就是右边的默认比左边的大/小
        def findRange(nums, MAX=True):
            stack = []
            L, R = list(range(len(nums))), list(range(len(nums)))
            if not MAX:
                nums = [-_ for _ in nums]
            for i in range(len(nums)):
                while stack and nums[i] >= nums[stack[-1]]:
                    j = stack.pop()
                    R[j] = i - 1
                L[i] = stack[-1] + 1 if stack else 0
                stack.append(i)
            while stack:
                j = stack.pop()
                R[j] = len(nums) - 1
            return L,R
        Lmax,Rmax = findRange(nums)
        Lmin,Rmin = findRange(nums,MAX=False)
        res = 0
        # 计算nums[i]为最大最小的区间个数
        for i in range(len(nums)):
            res += nums[i] * ((i - Lmax[i] + 1) * (Rmax[i] - i + 1) - (i - Lmin[i] + 1)*(Rmin[i] - i + 1))
        return res


if __name__ == '__main__':
    nums = [4, -2, -3, 4, 1]
    print(Solution.subArrayRanges2(nums))
