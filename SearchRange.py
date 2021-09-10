class Solution:
    @staticmethod
    def searchRange(nums, target: int):
        def RightBoundary(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2

                if target < nums[mid]:
                    r = mid
                elif target > nums[mid]:
                    l = mid + 1
                elif target == nums[mid]:
                    l = mid + 1

            if r == 0 or nums[r - 1] != target:
                return -1
            else:
                return r - 1

        def LeftBoundary(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                # print(l, r, mid)
                if target < nums[mid]:
                    r = mid
                elif target > nums[mid]:
                    l = mid + 1
                elif target == nums[mid]:
                    r = mid

            if l == len(nums) or nums[r] != target:
                return -1
            else:
                return r

        if len(nums) == 0:
            return [-1, -1]
        else:
            return [LeftBoundary(nums, target), RightBoundary(nums, target)]

    @staticmethod
    def searchRange2(nums, target: int):
        """
        闭区间解法
        :param nums:
        :param target:
        :return:
        """

        if len(nums) == 0:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[l] != target:
            return [-1, -1]

        a, b = l, len(nums) - 1
        while a < b:
            mid = (a + b + 1) // 2
            if nums[mid] <= target:
                a = mid
            else:
                b = mid - 1
        return [l, b]


if __name__ == '__main__':
    nums = [0, 1, 1, 1, 1, 1, 1]
    target = 1
    print(Solution.searchRange2(nums, target))
