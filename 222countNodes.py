#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/21 10:02
# @Author: Aaron Meng
# @File  : 222countNodes.py
from typing import List, Optional
from collections import deque

null = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 创建二叉树
class Tree(object):
    # 二叉树初始化函数
    @staticmethod
    def initTree(data):
        # 创建根结点，层序遍历
        if len(data) == 0:
            return None
        root = TreeNode(data[0])
        q = deque()
        cur_root = root
        flag = 0
        for i in range(1, len(data)):
            if data[i] is not None:
                cur_node = TreeNode(data[i])
                q.append(cur_node)
                if not flag:
                    cur_root.left = cur_node
                else:
                    cur_root.right = cur_node
            if flag:
                cur_root = q.popleft()
            flag ^= 1

        return root


class Solution:
    @staticmethod
    def countNodes(root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        node = root.left
        while node:
            node = node.left
            level += 1
        l = 1 << level
        r = (l << 1) - 1
        while l < r:
            mid = (l + r + 1) // 2
            node = root
            path = 1 << (level - 1)
            while node and path > 0:
                if mid & path:
                    node = node.right
                else:
                    node = node.left
                path >>= 1
            if node:
                l = mid
            else:
                r = mid - 1
        return r

    @staticmethod
    def countNodes2(root: TreeNode) -> int:
        lNode, rNode = root, root
        l = r = 0
        while lNode:
            lNode = lNode.left
            l += 1
        while rNode:
            rNode = rNode.right
            r += 1
        if l == r:
            return 2 ** l - 1
        return 1 + Solution.countNodes2(root.left) + Solution.countNodes2(root.right)


if __name__ == '__main__':
    root = [1, 2, 3, 4, 5, 6]
    root = Tree.initTree(root)
    print(Solution.countNodes(root))
    print(Solution.countNodes2(root))
