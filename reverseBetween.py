#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/16 14:22
# @Author: Aaron Meng
# @File  : reverseBetween.py
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 创建单链表
class LinkList(object):
    # 链表初始化函数, 方法类似于尾插
    @staticmethod
    def initList(data):
        # 创建头结点
        # 这个节点创建完，包含两部分：是个既包含节点值，也包含节点所链接的下一个节点
        if len(data) == 0:
            return None
        head = ListNode(data[0])

        # 初始化p指向头节点
        p = head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            # 构建完一个节点，移动到构建完的节点上，继续向后构建节点
            p = p.next

        return head

    # 遍历链表
    @staticmethod
    def traveList(head):
        # if self.isEmpty():
        #     exit(0)
        print("link list traveling result:")
        p = head
        while p:
            print(p.val, end='->')
            p = p.next
        print(None)

    # 获取链表总长度
    @staticmethod
    def getLength(head):
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        return n


class Solution:
    @staticmethod
    def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        prev, p = dummyHead, dummyHead.next
        for _ in range(left - 1):
            prev, p = prev.next, p.next
        q, end = p.next, p  # end of the sub-list
        for _ in range(left, right):
            end.next = q.next
            q.next = p
            prev.next = q
            p = prev.next
            q = end.next
        return dummyHead.next


if __name__ == '__main__':
    head = [1, 2]
    head = LinkList.initList(head)
    LinkList.traveList(head)
    left = 1
    right = 2
    head = Solution.reverseBetween(head, left, right)
    LinkList.traveList(head)
