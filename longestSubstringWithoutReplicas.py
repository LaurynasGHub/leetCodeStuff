class Solution:
    # METHODS- Hash Table, Sliding Window
    # first idea and try to solve this question
    def lengthOfLongestSubstring(self, s) -> int:
        seen = {}
        mLength = 0
        length = 0

        if len(s) == 1:
            return 1

        for i in range(0, len(s)):
            print('letter-',i , s[i])
            print('seen-', seen)

            if s[i] not in seen:
                seen[s[i]] = i
                length += 1
            else:
                # if len(seen) > length:
                #     length = len(seen)
                if length > mLength:
                    mLength = length

                seen = {}
                length = 1
                seen[s[i]] = i

        if len(seen) > mLength:
            mLength = len(seen)

        return mLength

    # answer method
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length


