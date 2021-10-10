class Solution:
    @staticmethod
    def searchInsert(nums, target: int) -> int:
        """
        开区间解法
        :param nums:
        :param target:
        :return:
        """
        l = 0  # left
        r = len(nums)  # right
        while l < r:
            mid = l + (r - l) // 2
            print(l, r, mid)
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return l

if __name__ == '__main__':
    # nums = [-2, -1, 0, 3, 5, 9, 12, 13]
    # target = 9
    nums = [-1, 0, 3, 5, 9, 12]
    target = 4
    print(Solution.searchInsert(nums, target))
