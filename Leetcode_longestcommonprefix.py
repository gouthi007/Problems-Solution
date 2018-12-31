'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        string = ""
        for i in range(len(strs)):
            if i == 0:
                    string = strs[i]
                    continue
            index = 0
            if i > 0:
                if len(string) <  len(strs[i]):
                    ll = string
                else:
                    ll = strs[i]
                for l in range(len(ll)):
                    if strs[i][l] == string[l]:
                        index += 1
                    else:
                        break
            string = strs[i][0:index]  
        return string
         
solution = Solution()
print(solution.longestCommonPrefix(["flower","flower","flower","fler"]))