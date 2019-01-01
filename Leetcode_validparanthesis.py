'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        stack = []
        bracketmapping = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        openbracket = ['(','{','[']
        for x in s:
            if x in openbracket:
                stack.append(x)
            elif stack and x == bracketmapping[stack[-1]]:
                stack.pop()
            else:
                return False 
        return stack == []
        







solution = Solution()
print(solution.isValid("{[(((())))]}"))