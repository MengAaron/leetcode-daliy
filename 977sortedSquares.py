class Solution:
    @staticmethod
    def sortedSquares(nums):
        n = len(nums)
        i, j, pos, ans = 0, n - 1, n - 1, [0] * n
        while i <= j:
            if nums[i] * nums[i] < nums[j] * nums[j]:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            else:
                ans[pos] = nums[i] * nums[i]
                i += 1
            pos -= 1
        return ans


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(Solution.sortedSquares(nums))