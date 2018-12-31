"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

class Solution:
    def twoSum(self, nums, target):
        """
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        for i, val in enumerate(nums):
            j = len(nums) - 1
            while i < j:
                if (nums[i] + nums[j] == target):
                    return [i+1,j+1]
                elif (nums[i] + nums[j] > target):
                    j -= 1
                elif (nums[i] + nums[j] < target):
                    i += 1

nums = [2, 7, 11, 15, 20]
target = 26

solution = Solution()
print(solution.twoSum(nums, target))