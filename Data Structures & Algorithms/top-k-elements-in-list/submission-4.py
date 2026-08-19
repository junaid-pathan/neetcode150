class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {} 
        for val in nums: 
            dict1[val] = dict1.get(val,0)+1 

        freq = [[] for i in range(len(nums)+1)]

        items = dict1.items()
        for key,val in items: 
            freq[val].append(key)  
        res = []
        for i in range(len(freq)-1,0,-1): 
            for n in freq[i]: 
                res.append(n)
                if len(res)==k:
                    return res

