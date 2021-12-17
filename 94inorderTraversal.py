#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/16 13:06
# @Author: Aaron Meng
# @File  : 94inorderTraversal.py
from typing import List, Optional
from queue import Queue

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
        q = Queue()
        cur_root = root
        flag = 0
        for i in range(1, len(data)):
            if data[i] is not None:
                cur_node = TreeNode(data[i])
                q.put(cur_node)
                if not flag:
                    cur_root.left = cur_node
                else:
                    cur_root.right = cur_node
            if flag:
                cur_root = q.get()
            flag ^= 1

        return root


class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        # Morris
        ans = []
        cur = root
        while cur:
            mostRight = cur.left
            if mostRight:
                while mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right
                if mostRight.right:
                    mostRight.right = None
                else:
                    mostRight.right = cur
                    cur = cur.left
                    continue
            ans.append(cur.val)
            cur = cur.right
        return ans

    @staticmethod
    def inorderTraversal2(root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


if __name__ == '__main__':
    root = [1, 2, 3, 4, 5, 6, 7]
    root = Tree.initTree(root)
    print(Solution.inorderTraversal2(root))
