#
# QUESTION no- 5
# METHODS- Two Pointers, Dynamic Programming
# 
# my solution, doesn't work with edge cases
class Solution:
  s = "aacabdkacaa"
  
    def longestPalindrome(s):
        left = 0
        right = len(s) - 1

        if len(s) == 1:
            return s

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        while left < right:
            if s[left] != s[right]:
                right -= 1
            else:
                return s[left: right + 1]
                
            if right == left:
                right = len(s) - 1
                left += 1

    longestPolindrome(s)

    # Expand from centers solution
    def longestPalindrome(self, s):
        # function finds the string
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        # result always holds the longest string encountered so far
        result = ""
        # go trough input array
        for i in range(len(s)):
            # check when the string length is odd
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
            # check when the string length is even
            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2
        return result
