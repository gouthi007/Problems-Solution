"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        numsSorted = sorted(nums)
        for ind in range(len(numsSorted)):
            last = len(numsSorted) -1
            while last > ind:
                if numsSorted[ind] + numsSorted[last] == target:
                    if numsSorted[ind] != numsSorted[last]:
                       return [nums.index(numsSorted[ind]), nums.index(numsSorted[last])]
                    else:
                        gouthi = list()
                        for x in range(len(nums)):
                            if numsSorted[ind] == nums[x]:
                                gouthi.append(x)
                        return [gouthi[0],gouthi[1]] 
                elif numsSorted[ind] + numsSorted[last] > target:                
                    last -= 1
                elif numsSorted[ind] + numsSorted[last] < target:
                    break
nums = [3, 2, 3]
target = 6
solution = Solution()
print(solution.twoSum(nums, target))