class solution:
    
    s = 'abc'
    t = 'ahbgdc'
    
    def isSubsequence(s, t):
        
        sS = [*s]
        tS = [*t]
        
        i = 0
        a = 0
        
        if len(s) == 0:
            return False
        
        while i < len(t) + 1:
            if sS[a] == tS[i]:
                a += 1
            
            if a == len(s):
                print('return-', True)
                return True
            
            i += 1

        return False   
        
    isSubsequence(s, t)
            