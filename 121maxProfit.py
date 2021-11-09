#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/25 20:19
# @Author: Aaron Meng
# @File  : 121maxProfit.py
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(price - min_price, max_profit)
        return max_profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution.maxProfit(prices))
