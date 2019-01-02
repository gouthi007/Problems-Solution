"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return (s[len(s)::-1])

solution = Solution()
print(solution.reverseString("A man, a plan, a canal: Panama"))
        