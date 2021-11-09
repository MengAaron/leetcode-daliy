#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/11/5 16:52
# @Author: Aaron Meng
# @File  : 319bulbSwitch.py
from typing import List
import math

class Solution:
    @staticmethod
    def bulbSwitch(n: int) -> int:
        return int(math.sqrt(n))


if __name__ == '__main__':
    n = 5
    print(Solution.bulbSwitch(n))
