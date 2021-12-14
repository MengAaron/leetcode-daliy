#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/12 11:14
# @Author: Aaron Meng
# @File  : 5954minimumRefill.py
from typing import List


class Solution:
    @staticmethod
    def minimumRefill(plants: List[int], capacityA: int, capacityB: int) -> int:
        cnt = 0
        A, B = capacityA, capacityB
        i, j = 0, len(plants) - 1
        while i < j:
            if A < plants[i]:
                A = capacityA - plants[i]
                cnt += 1
            else:
                A -= plants[i]
            if B < plants[j]:
                B = capacityB - plants[j]
                cnt += 1
            else:
                B -= plants[j]
            i += 1
            j -= 1
        if i == j and max(A, B) < plants[i]:
            cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution.minimumRefill(
        plants=[726, 739, 934, 116, 643, 648, 473, 984, 482, 85, 850, 806, 146, 764, 156, 66, 186, 339, 985, 237, 662,
                552, 800, 78, 617, 933, 481, 652, 796, 594, 151, 82, 183, 241, 525, 221, 951, 732, 799, 483, 368, 354,
                776, 175, 974, 187, 913, 842],
        capacityA=1439, capacityB=1207))
