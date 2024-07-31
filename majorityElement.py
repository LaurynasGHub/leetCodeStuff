# 
# QUESTION no. 169
# METHODS- Python Dictionary, Hash Table, Array, Counting
# 
class Solution(object):
    def majorityElement(self, nums):
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] = seen.get(nums[i]) + 1
        
        # print(max(seen, key=seen.get))
        return max(seen, key=seen.get)
        # print(seen)
