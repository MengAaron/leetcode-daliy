from typing import List


class Solution:
    @staticmethod
    def minSubArrayLen(target: int, nums: List[int]) -> int:
        tempSum, tempLen, tempList, ansLen, ansList = 0, 0, [], 1e5+1, []
        j = 0
        for i in range(len(nums)):
            tempSum += nums[i]
            tempLen += 1
            tempList.append(nums[i])
            if tempSum < target:
                continue
            while tempSum >= target:
                tempSum -= nums[j]
                tempLen -= 1
                j += 1
            j -= 1
            tempSum += nums[j]
            tempLen += 1
            # print(i, j, tempSum, ansLen)
            if tempLen < ansLen:
                ansLen = tempLen
        if tempSum < target:
            return 0
        else:
            return ansLen


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution.minSubArrayLen(target, nums))
