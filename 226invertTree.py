#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/18 12:51
# @Author: Aaron Meng
# @File  : 226invertTree.py
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

    @staticmethod
    def levelOrder(root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append((0, root))
        while q:
            level, cur = q.popleft()
            if len(ans) <= level:
                ans.append([cur.val])
            else:
                ans[level].append(cur.val)
            if cur.left:
                q.append((level + 1, cur.left))
            if cur.right:
                q.append((level + 1, cur.right))
        return ans


class Solution:
    @staticmethod
    def invertTree(root: TreeNode) -> TreeNode:
        if not root:
            return root
        temp = root.left
        root.left = Solution.invertTree(root.right)
        root.right = Solution.invertTree(temp)
        return root

if __name__ == '__main__':
    root = [1, 2, 3, 4, 5, 6, 7]
    root = Tree.initTree(root)
    print(Tree.levelOrder(root))
    root = Solution.invertTree(root)
    print(Tree.levelOrder(root))
