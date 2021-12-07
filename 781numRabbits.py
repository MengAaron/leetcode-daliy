#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/14 21:25
# @Author: Aaron Meng
# @File  : 781numRabbits.py
from typing import List
from collections import Counter
import math


class Solution:
    @staticmethod
    def numRabbits(answers: List[int]) -> int:
        if not answers:
            return 0
        cnt = Counter(answers)
        res = 0
        for k, v in cnt.items():
            res += math.ceil(v / (k + 1)) * (k + 1)
        return res


if __name__ == '__main__':
    answers = [10, 10, 10]
    print(Solution.numRabbits(answers))
