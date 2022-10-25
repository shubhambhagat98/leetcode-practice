class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        key = "$##%"
        
        output = key.join(strs)
        print(output)
        
        return output
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        key = "$##%"
        output = s.split(key)
        print(output)
        return output
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))