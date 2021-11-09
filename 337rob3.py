#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/25 16:59
# @Author: Aaron Meng
# @File  : 337rob3.py
from typing import List
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(nums: list) -> TreeNode:
    if not nums:
        return None
    if not nums[0]:
        return None
    q = Queue()
    n = len(nums)
    root = TreeNode(val=nums[0])
    q.put(root)
    for i in range(1, n, 2):
        cur_root = q.get()
        if nums[i]:
            left = TreeNode(nums[i])
            q.put(left)
        else:
            left = None
        if nums[i + 1]:
            right = TreeNode(nums[i + 1])
            q.put(right)
        else:
            right = None
        cur_root.left = left
        cur_root.right = right

    return root


class Solution:
    @staticmethod
    def rob3(root: TreeNode) -> int:
        def _rob(root: TreeNode) -> (int, int):
            if not root:
                return 0, 0  # 偷，不偷
            left = _rob(root.left)
            right = _rob(root.right)
            v1 = root.val + left[1] + right[1]  # 偷
            v2 = max(left) + max(right)  # 不偷
            return v1, v2

        return max(_rob(root))


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 3, None, 1]
    root = construct(nums)
    print(Solution.rob3(root))
