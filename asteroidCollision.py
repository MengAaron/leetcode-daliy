#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/10/27 10:05
# @Author: Aaron Meng
# @File  : asteroidCollision.py
from typing import List


class Solution:
    @staticmethod
    def asteroidCollision(asteroids: List[int]) -> List[int]:
        stack = [-1001]
        for a in asteroids:
            while True:
                if stack[-1] < 0 or a > 0:
                    stack.append(a)
                    break
                elif a + stack[-1] < 0:
                    stack.pop()
                elif a + stack[-1] > 0:
                    break
                else:
                    stack.pop()
                    break
        return stack[1:]


if __name__ == '__main__':
    asteroids = [5, -5]
    print(Solution.asteroidCollision(asteroids))
