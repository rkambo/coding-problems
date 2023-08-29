class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retArray = [1] * len(nums)
        
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            retArray[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            retArray[i] *= postfix
            postfix *= nums[i]
        return retArray