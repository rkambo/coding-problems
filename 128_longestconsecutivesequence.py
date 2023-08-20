class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0
        currStreak = 0
        
        for n in nums:
            if (n-1) not in numSet:
                currStreak = 0
                while (n + currStreak) in numSet: 
                    currStreak += 1
                longestStreak = max(longestStreak,currStreak)
        return longestStreak