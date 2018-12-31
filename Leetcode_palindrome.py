"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #print(id(x))
        x = str(x)
        #print(id(x))
        temp = str(x)
        #rint(id(temp))
        temp = temp[::-1]
        #print(id(temp))
        if x.lstrip() == temp.lstrip():
            return (True)
        else:
            return (False)

solution = Solution()
print(solution.isPalindrome(12321))