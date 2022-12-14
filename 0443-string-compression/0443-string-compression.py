class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1
        
        curr = 1
        count = 1
        
        s = ""
        
        while curr < len(chars):
            if chars[curr-1] == chars[curr]:
                count += 1
            else:
                s+= chars[curr-1]  
                if count > 1:
                    s+= str(count)
                    count = 1
            curr += 1
                
        if count == 1:
            s+= chars[curr-1]
        else:
            s+= chars[curr-1] + str(count)     
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s) 
        