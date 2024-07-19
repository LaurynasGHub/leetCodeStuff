class solution:
    
    eglute = [1,8,6,2,5,4,8,3,7]
    
    def solution(height):
        
        # pointer for highest number
        left = 0
        # pointer for second number
        right = 0
        # diff between columns
        diff = 0
        # find leftmost number
        # find rightmost number
        i = 0
        a = 0
        area = 0
        
        while i < len(height)-1:
            # print('<-------> i-', i)
            
            left = height[i]
            right = height[a]
            
            # print('left = ', left, 'right = ', right)
            
            if right > left:
                # print('r > l = ', right - left)
                area = (right - (right- left)) * left
            else:
                # print('l > r = ', left - right)
                area = (left - (left - right)) * right
            
            print(i, 'area-', area)
            i += 1
    
    # solution(eglute)
    
    # solution from leetcode
    def solutionv2(height):
        left = 0
        right = len(height) - 1
        maxArea = 0

        # one pointer comes in from the end of the array (right), other comes in from the start (left)
        while left < right:
            print('left = ', left, 'right = ', right)
            # calculate area starting from the end, get min number between left and right and multiply by their difference
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
    
    solutionv2(eglute)