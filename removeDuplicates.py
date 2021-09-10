class Solution:
    @staticmethod
    def removeDuplicates(nums):
        """双指针"""
        if len(nums) <= 1:
            return len(nums)
        j = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j+1


if __name__ == '__main__':
    nums = [1]
    print(Solution.removeDuplicates(nums))