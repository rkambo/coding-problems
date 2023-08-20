class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) <= 1):
            return False
        nums.sort()
        
        for x in range(len(nums)-1):
            if(nums[x] == nums[x+1]):
                return True
        return False 