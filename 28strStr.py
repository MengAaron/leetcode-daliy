#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/9/29 10:00
# @Author: Aaron Meng
# @File  : strStr.py
from typing import List


class Solution:
    @staticmethod
    def strStrEnumerate(haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        if m == 0 or n > m:
            return -1
        for i in range(m):
            if n > m - i:
                break
            flag = 1
            for j in range(n):
                if i + j == m or haystack[i + j] != needle[j]:
                    flag = 0
                    break
            if flag:
                return i
        return -1

    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        if m == 0 or n > m:
            return -1
        next = [0 for _ in range(n)]
        # contrust next
        k = 0
        for i in range(1, n):
            while k and needle[i] != needle[k]:
                k = next[k - 1]
            if needle[i] == needle[k]:
                next[i] = k + 1
                k += 1
        # match
        i = 0
        for j in range(m):
            while i and haystack[j] != needle[i]:
                i = next[i-1]
            if haystack[j] == needle[i]:
                i += 1
            if i == n:
                return j - n + 1
        return -1


if __name__ == '__main__':
    haystack = "ababcaababcaabc"
    needle = "ababcaabc"
    print(Solution.strStr(haystack, needle))
