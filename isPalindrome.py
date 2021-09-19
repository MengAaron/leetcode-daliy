#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/18 11:21
# @Author: Aaron Meng
# @File  : isPalindrome.py
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
    def isPalindrome(head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        result = []
        slow, fast = head, head
        length = 0
        while fast:
            length += 1
            if length % 2 == 0:
                result.append(slow.val)
                slow = slow.next
            fast = fast.next
        if length % 2 != 0:
            slow = slow.next
        while slow:
            if slow.val != result.pop():
                return False
            slow = slow.next

        return True


if __name__ == '__main__':
    head = [1, 2,1]
    head = LinkList.initList(head)
    LinkList.traveList(head)
    print(Solution.isPalindrome(head))
