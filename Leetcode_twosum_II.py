'''Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.'''
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

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))