"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threesum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        s = set()
        for ind, val in enumerate(nums):
            left = ind + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + val + nums[right]
                if sum == 0:
                    s.add((val,nums[left],nums[right]))
                # if nums[left] == nums[right]
                    #break
                    left += 1
                    right -= 1
                if sum > 0:
                    right -= 1
                if sum < 0:
                    left += 1
        return list(s)



solution = Solution()
print(solution.threesum([-1, 0, 1, 2, -1, -4]))


