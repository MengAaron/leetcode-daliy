#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/30 19:51
# @Author: Aaron Meng
# @File  : 110isBalanced.py
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
    def isBalanced(root: TreeNode) -> bool:
        def height(root: TreeNode):
            if not root:
                return 0
            leftH = height(root.left)
            rightH = height(root.right)
            if leftH == -1 or rightH == -1 or abs(leftH - rightH) > 1:
                return -1
            return max(leftH, rightH) + 1

        return height(root) > -1


if __name__ == '__main__':
    root = [1,2,2,3,3,null,null,4,4]
    root = Tree.initTree(root)
    print(Solution.isBalanced(root))
