#
# QUESTION no. 55
# METHODS- Greedy
#
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            print('i-', i, 'nums[i]-',nums[i])
            if i + nums[i] >= goal:
                goal = i
                print('goal-',goal)
        
        return True if goal <= 0 else False
