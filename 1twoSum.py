class Solution:
    @staticmethod
    def twoSum(nums, target):
        k = len(nums)
        for i in range(k):
            j = i + 1
            while j <= k - 1:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution.twoSum(nums, target))
