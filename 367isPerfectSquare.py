class Solution:
    @staticmethod
    def isPerfectSquare(num: int) -> bool:
        if num == 0 or num == 1:
            return True
        l, r = 0, num
        while l < r:
            mid = l + (r - l) // 2
            if mid * mid > num:
                r = mid
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False


if __name__ == '__main__':
    # nums = [-2, -1, 0, 3, 5, 9, 12, 13]
    # target = 9
    for x in range(100):
        print(x, Solution.isPerfectSquare(x))
    # print(Solution.mySqrt(2))
