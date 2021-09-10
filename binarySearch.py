class Solution:
    @staticmethod
    def search1(nums, target: int) -> int:
        """
        开区间解法
        :param nums:
        :param target:
        :return:
        """
        l = 0  # left
        r = len(nums)  # right
        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1

    @staticmethod
    def search2(nums, target: int) -> int:
        """
        闭区间解法
        :param nums:
        :param target:
        :return:
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1

        return -1

    @staticmethod
    def search3(nums, target: int) -> int:
        """
        截断区间解法
        :param nums:
        :param target:
        :return:
        """
        offset = 0
        while True:
            mid = len(nums) // 2
            print(nums)
            print(mid)
            if target == nums[mid]:
                return offset + mid
            elif len(nums) <= 1:
                return -1
            elif target > nums[mid]:
                nums = nums[mid:]
                offset += mid
            elif target < nums[mid]:
                nums = nums[:mid]


if __name__ == '__main__':
    # nums = [-2, -1, 0, 3, 5, 9, 12, 13]
    # target = 9
    nums = [-1, 0, 3, 5, 9, 12]
    target = 5
    print(Solution.search2(nums, target))
