class solution:
    
    s = 'ab'
    t = 'ahbgdc'
    
    def isSubsequence(s, t):
        
        sS = [*s]
        tS = [*t]
        
        i = 0
        a = 0
        
        while i < len(t):
            if a == len(s):
                print('return-', True)
                return True
            
            if sS[a] == tS[i]:
                a += 1
            
            i += 1

        return False
        
        
        
    isSubsequence(s, t)
            