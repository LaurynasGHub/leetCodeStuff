# 
# QUESTION no- 1679
# METHODS- Hash Table, Two Pointers, Array
# 
class solution:
    
    nums = [1,2,3,4]
    k = 5
    
    def maxOperations(nums, k):
        nums.sort()
        left = 0
        right = len(nums) - 1
        times = 0
        
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                times += 1
            else:
                left += 1
                right -= 1

        print(times)
        return times

    maxOperations(nums, k)
