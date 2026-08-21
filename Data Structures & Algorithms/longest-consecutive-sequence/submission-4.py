class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        longest = 0 
        for value in sets:  
            if value-1 not in sets:
                length=1  
                while (value+length) in sets:
                    length+=1   
                if length>longest:
                    longest = length 
        return longest 
        