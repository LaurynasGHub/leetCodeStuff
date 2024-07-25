# 
# QUESTION no- 26
# METHODS- Two Pointers, Array
# 
class Solution:
  nums = [1, 1, 2]
  nums2 = [0,0,1,1,1,2,2,3,3,4]
  
	def removeDuplicates(self, nums):
		slow, fast = 0, 1
    # while slow pointer is in range of given array
		while fast in range(len(nums)):
      # if nums in slow and fast places are identical move fast forward
			if nums[slow] == nums[fast]:
				fast += 1
      # if nums aren't identical then replace number to the right of slow to fast
			else:
				nums[slow+1] = nums[fast]
				fast += 1
				slow += 1

		return slow + 1
