# my solution doesn't work with edge cases

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
