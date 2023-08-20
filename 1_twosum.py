class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for x in range(len(nums)):
            complement = target - nums[x]
            if(dictionary.get(complement) != None):
                return [dictionary.get(complement),x]
            dictionary[nums[x]] = x
        return []