#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/29 13:13
# @Author: Aaron Meng
# @File  : 93restoreIpAddresses.py
from typing import List


class Solution:
    @staticmethod
    def restoreIpAddresses(s: str) -> List[str]:
        res = []
        path = []
        n = len(s)
        def pieceValid(i,j):
            if i == j:
                return True
            if s[i] == '0':
                return False
            if 9<int(s[i:j+1])<256:
                return True
        def backtracking(count=4,start=0):
            if count == 0:
                if start == n:
                    res.append('.'.join(path))
                return
            for i in range(start,start+3):
                if pieceValid(start,i) and count <= n-i <= 3*count:
                    path.append(s[start:i+1])
                    backtracking(count-1,i+1)
                    path.pop()
        backtracking()
        return res



if __name__ == '__main__':
    s = "00001"
    print(Solution.restoreIpAddresses(s))
