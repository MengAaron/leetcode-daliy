#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/14 21:07
# @Author: Aaron Meng
# @File  : 714maxProfit.py
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        lastdp0, lastdp1 = -prices[0], 0
        for i in range(1, n):
            dp0 = max(lastdp0, lastdp1 - prices[i])
            dp1 = max(lastdp0 + prices[i] - fee, lastdp1)
            lastdp0, lastdp1 = dp0, dp1
        return dp1


if __name__ == '__main__':
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    print(Solution.maxProfit(prices, fee))
