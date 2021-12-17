#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/16 11:27
# @Author: Aaron Meng
# @File  : 145postorderTraversal.py
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
    def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:    # 没有右子节点或者右子节点已经被访问
                ans.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return ans

    @staticmethod
    def postorderTraversal2(root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        ans.extend(Solution.postorderTraversal2(root.left))
        ans.extend(Solution.postorderTraversal2(root.right))
        ans.append(root.val)
        return ans

    @staticmethod
    def postorderTraversal3(root: Optional[TreeNode]) -> List[int]:
        # Morris
        ans = []
        dummyTreeNode = TreeNode(left=root)
        root = dummyTreeNode
        def rightEdge(node):
            res = []
            while node:
                res.append(node.val)
                node = node.right
            res.reverse()
            return res
        while root:
            mostRight = root.left
            if mostRight:
                while mostRight.right and mostRight.right != root:
                    mostRight = mostRight.right
                if mostRight.right:
                    mostRight.right = None
                    ans.extend(rightEdge(root.left))
                else:
                    mostRight.right = root
                    root = root.left
                    continue
            root = root.right
        return ans




if __name__ == '__main__':
    root = [1, 2, 3, 4, 5, 6, 7]
    root = Tree.initTree(root)
    print(Solution.postorderTraversal(root))
    print(Solution.postorderTraversal2(root))
    print(Solution.postorderTraversal3(root))
