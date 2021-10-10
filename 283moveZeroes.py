class Solution:
    @staticmethod
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        j = -1
        for i in range(0, len(nums)):
            print(j,i,nums)
            if nums[i] != 0:
                nums[j+1] = nums[i]
                j += 1
                if i>j:
                    nums[i] = 0

        return nums



if __name__ == '__main__':
    nums = [1,0]
    print(Solution.moveZeroes(nums))