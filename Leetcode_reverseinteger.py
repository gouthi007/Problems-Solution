"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
"""

class Solution:
    def reverse(self, x):
        reverse1 = 0
        flag = 0
        reversee1 = str(x)
        while x != 0:
                if x < 0:
                    x = x * (-1)
                    flag = 1
                pop = x%10
                x = x//10
                if int(reverse1) >= 2**31-1 or int(reverse1) <= -2**31:
                    return 0    
                reverse1 = reverse1 * 10 + pop
                if int(reverse1) >= 2**31-1 or int(reverse1) <= -2**31: 
                    return 0
        if flag == 1:
                reverse1 = str(reverse1)
                reversee1 = "-"+ reverse1
                return (int(reversee1))
        return int(reverse1)
solution = Solution()
print(solution.reverse(123))