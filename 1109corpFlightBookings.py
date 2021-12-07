#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/9 16:50
# @Author: Aaron Meng
# @File  : 1109corpFlightBookings.py
from typing import List


class Solution:
    @staticmethod
    def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for _ in range(n)]
        for first, last, seats in bookings:
            for i in range(first - 1, last):
                ans[i] += seats
        return ans

    @staticmethod
    def corpFlightBookings2(bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for _ in range(n)]
        for first, last, seats in bookings:
            ans[first - 1] += seats
            if last < n:
                ans[last] -= seats
        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans


if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(Solution.corpFlightBookings2(bookings, n))
