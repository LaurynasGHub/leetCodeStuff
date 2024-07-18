# this solutions returns what is expected but gives some compiler error
# compiler problem is on leetcode side
# still can't completely understand the problem

class solution:
    
    chars = ["a","a","b","b","c","c","c"]

    def compress(chars):
        char = chars[0]
        unique_chars = [chars[0]]

        for i in chars:
            if i != char:
                char = i
                unique_chars.append(i)
        
        frequency = []
        
        for i in unique_chars:
            freq = 0
            
            for a in chars:
                if i == a:
                    freq += 1
            
            frequency.append(freq)

        return_list = []
        
        for i in range(0, len(unique_chars)):
            return_list.append(unique_chars[i])
            return_list.append(frequency[i])
        
        print('unique_chars-', unique_chars)
        print('frequency-', frequency)
        print('return_list-',return_list)
        
        return return_list
    

    compress(chars)
    
    #this solution works and compiles in leetcode
    
    def compress_v2(chars):
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
                
            chars[ans] = letter
            ans += 1
            
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1

        return ans
    
    compress_v2(chars)