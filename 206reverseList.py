#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/14 20:54
# @Author: Aaron Meng
# @File  : reverseList.py
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
    def reverseList(head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p, q = head, head.next
        p.next = None
        while q:
            temp = q.next
            q.next = p
            p = q
            q = temp
        return p



if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    head = LinkList.initList(head)
    LinkList.traveList(head)
    # reverse
    head = Solution.reverseList(head)
    LinkList.traveList(head)
