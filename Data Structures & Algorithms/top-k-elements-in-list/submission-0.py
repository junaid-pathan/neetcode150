class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {} 
        for i in range(len(nums)): 
            if nums[i] in dict1: 
                dict1[nums[i]]+=1 
            else: 
                dict1[nums[i]]=1 
        items = list(dict1.items())
        sortedvalues = sorted(items, key= lambda x:x[1], reverse=True)
        finalvalues = sortedvalues[0:k]
        result = [i[0] for i in finalvalues]
        return result
        
        