class Solution:

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


