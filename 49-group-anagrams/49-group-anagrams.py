class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index  = 0
        op = []
        d = {}
        for string in strs:
            temp = "".join(sorted(string))
            print(temp)
            if d.get(temp) is not None:
                op[d.get(temp)].append(string)
            else:
                d[temp] = index
                op.append([string])
                index+=1
                
        return op
        
                