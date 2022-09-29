class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        for x in nums:
            if x not in d:
                d[x] = (x, 1)
            else:
                d[x] = (x, d[x][1]+1)
        
        temp = list(d.values())
        temp.sort(key = lambda x: x[1], reverse = True)
        
        op = []

        for i in range(k):
            op.append(temp[i][0])

        return op