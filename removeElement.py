class Solution:
    @staticmethod
    def removeElement(nums, val: int):
        """双指针"""
        l, r = 0, len(nums)
        while l < r:
            if nums[r - 1] == val:
                r -= 1
            elif nums[l] == val:
                nums[l] = nums[r - 1]
                r -= 1
            else:
                l += 1
        return r


if __name__ == '__main__':
    nums = [-1, 0, 5, 3, 5, 5, 9, 12]
    val = 5
    print(Solution.removeElement(nums, val))
