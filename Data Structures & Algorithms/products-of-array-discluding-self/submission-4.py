class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prod = [1]*size
        before = [1]*size
        after = [1]*size
        #just trying to pre compute the prods before the 
        before[0] = 1 
        after[size-1] = 1
        for i in range(1,size): 
            before[i] = before[i-1] * nums[i-1]
        for j in range(size-2,-1,-1): 
            after[j] = after[j+1] * nums[j+1]
        for k in range(size): 
            prod[k] = before[k]*after[k]
        return prod


        