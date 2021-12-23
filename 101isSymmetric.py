#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/19 14:48
# @Author: Aaron Meng
# @File  : 101isSymmetric.py
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
    def isSymmetric(root: TreeNode) -> bool:
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if (not right) and (not left):
                continue
            if (not right) or (not left) or right.val != left.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

    @staticmethod
    def isSymmetric2(root: TreeNode) -> bool:
        def check(node1: TreeNode,node2: TreeNode):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and check(node1.left,node2.right) and check(node1.right,node2.left)
        return check(root.left,root.right)
if __name__ == '__main__':
    root = [1, 2, 2, 3, 4, 4, 3]
    root = Tree.initTree(root)
    print(Solution.isSymmetric2(root))
