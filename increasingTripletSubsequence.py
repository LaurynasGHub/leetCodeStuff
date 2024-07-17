class Solution:
  nums = [1,2,3,4,5,6]

  # solution 1, gives false on cases where triplets increase non contiguously
  # [20,100,10,12,5,13] should give True, because
  # 10,12,13
  
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range (0, len(nums)-2):
            print ('i-',i)
            if i == len(nums)-1:
                break

            triplet = [nums[i], nums[i+1], nums[i+2]]
            print ('triplet-', triplet)

            if triplet[0] < triplet[1] and triplet[1] < triplet[2]:
                return True
        
        return False
      
# solution 2 gives True on case from solution 1, but is very slow

def solution2(self, nums: List[int]) -> bool:
        for i in range (0, len(nums)-2):
            for a in range (i, len(nums)-1):
                if nums[i] < nums[a]:
                    for b in range(a, len(nums)):
                        if nums[a] < nums[b]:
                            return True

  # solution 3, trying to optimize it
  
  def solution3(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # init first smallest and second smallest as infinite values
        first = float('inf')
        second = float('inf')
        # itterate the array
        for n in nums:
            # if n is smaller than the number than change them
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                return True  # found a triplet
        
        return False
