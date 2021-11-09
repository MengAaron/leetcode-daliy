#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/26 17:55
# @Author: Aaron Meng
# @File  : 123maxProfit.py
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        buy1 = prices[0]  # 第一次买入
        sell1 = 0  # 第一次卖出
        buy2 = prices[0]
        sell2 = 0
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)  # 第二次买入成本降低
            sell2 = max(sell2, price - buy2)
        return sell2


if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    print(Solution.maxProfit(prices))
