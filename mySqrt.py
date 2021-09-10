class Solution:
    @staticmethod
    def mySqrt(x: int) -> int:
        if x == 1:
            return 1
        l, r = 1, x
        mid = -1
        while l < r:
            mid = l + (r - l + 1) // 2
            # print(l,r,mid)
            if (mid) * (mid) > x:
                r = mid - 1
            elif (mid) * (mid) < x:
                l = mid
            else:
                return mid
        return r
if __name__ == '__main__':
    # nums = [-2, -1, 0, 3, 5, 9, 12, 13]
    # target = 9
    for x in range(100):
        print(x, Solution.mySqrt(x))
    # print(Solution.mySqrt(2))
