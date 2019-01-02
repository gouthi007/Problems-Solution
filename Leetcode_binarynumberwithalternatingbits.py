'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

'''
class Solution(object):
    def hasAlternatingBits(self, n):
        n = bin(n)
        n = n.lstrip("0b")
        for x in range(1, len(n)):
            if n[x] != n[x-1]:
                continue
            else:
                return False
        return True


solution = Solution()
print(solution.hasAlternatingBits(4))
                




