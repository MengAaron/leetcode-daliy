#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/14 11:19
# @Author: Aaron Meng
# @File  : 309maxProfit.py
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        # 0持有，1卖出，2观望
        n = len(prices)
        dp = [[-prices[0], 0, 0]] + [[0, 0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1])

    @staticmethod
    def maxProfit2(prices: List[int]) -> int:
        # 0持有，1卖出，2观望
        n = len(prices)
        dp = (-prices[0], 0, 0)
        for i in range(1, n):
            dp0 = max(dp[0], dp[2] - prices[i])
            dp1 = dp[0] + prices[i]
            dp2 = max(dp[1], dp[2])
            dp = (dp0, dp1, dp2)
        return max(dp)


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    print(Solution.maxProfit(prices))
