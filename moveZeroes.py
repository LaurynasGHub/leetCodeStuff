# 
# QUESTION no- 283
# METHODS- Two Pointers
# 
nums = [0, 0, 1, 0, 2, 0, 0, 1]
nums2 = [0,0,0,0,0,0,1,1,1]

#using new array
def moveZeroes(nums):
    
    return_array = []
    zeroes = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            return_array.append(nums[i])
        else:
            zeroes += 1
    
    for i in range(zeroes):
        return_array.append(0)
    
    print('zeroes-', zeroes)
    print('return_array-', return_array)

# moveZeroes(nums)
        
# without using new array
def moveZeroesv2(nums):
    
    i = 0
    pos = 0
    
    for i in range(len(nums)):
        print (i, '-', nums[i])
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            pos = i 
    
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    
    if nums[0] == 0:
        nums.pop(0)
        nums.append(0)
    
    print(pos)
    print(nums)

moveZeroesv2(nums2)

def moveWithoutZeroesv3(nums):
    non_zero = 0  # Pointer for non-zero elements
        
    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            non_zero += 1
        
