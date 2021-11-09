#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/25 20:30
# @Author: Aaron Meng
# @File  : 122maxProfit.py
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        profit = 0
        buying_price = prices[0]
        for price in prices[1:]:
            if price> buying_price:
                profit += price - buying_price
            buying_price = price
        return profit




if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution.maxProfit(prices))
