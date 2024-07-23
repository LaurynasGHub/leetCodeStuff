class Solution:
    nums = [1,12,-5,-6,50,3]
    # this solution gives time limit error on edge case
    def findMaxAverage(self, nums):
        mSum = cSum = float(-inf)

        for i in range(len(nums) - k + 1):
            cSum = sum(nums[i : i + k])

            if cSum > mSum:
                mSum = cSum

        return mSum / k

        # for i in range(len(nums) - k):
        #     cSum = 0
        #     for a in range(i, i + k):
        #         cSum += nums[a]
            
        #     if cSum > mSum:
        #         mSum = cSum
            
        # return mSum / k
    # good solution
    def findMaxAverage2(self, nums):
        # get first sum, to the left from k
        window = sum(nums[:k])
        max_sum = window
        
        for i in range(len(nums) - k):
            # 
            window = window - nums[i] + nums[i + k]
            max_sum = max(max_sum, window)
        
        return max_sum / k
