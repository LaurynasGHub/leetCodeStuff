# 
# QUESTION no- 1456
# METHODS- Sliding Window
# 
class Solution:
    string = ['asdawdasd']

    # again time limit exceeded on edge case
    def maxVowels(self, s):
        # vowels = ['a', 'e', 'i', 'o', 'u']
        vowels ='aeiou'
        mVow = 0

        for i in range(len(s) - k +1):
            vCount = 0
            lArr = s[i: i + k]
            # print(lArr, 'vCount-', vCount)
            for l in lArr:
                # print('l-', l)
                if l in vowels:
                    vCount += 1
                    # print('add-', l, vCount)
            if vCount > mVow:
                mVow = vCount
            
        return mVow

    # second method, no errors
    def maxVowels2(self, s):
        # vowels = ['a', 'e', 'i', 'o', 'u']
        vowels ='aeiou'
        cVow = 0

        for i in s[:k]:
            if i in vowels:
                cVow += 1

        mVow = cVow

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cVow -= 1
            
            if s[i] in vowels:
                cVow += 1
            
            mVow = max(mVow, cVow)
        
        return mVow
