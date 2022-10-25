class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        key = "#"
        op = ""
        for s in strs:
            op += str(len(s)) + key + s
        
        
        return op
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        key = "#"
        op = []
        i= 0
        
        while i < len(s):
            key_index = s.index(key, i)
            word_length = int(s[i:key_index])
            
            op.append(s[key_index+1 : key_index+1 + word_length])
            
            i = key_index+1 + word_length
            
        
        return op


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))