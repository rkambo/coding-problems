class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ret = right
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for pile in piles:
                count += ceil(pile / mid)
            if count <= h:
                ret = min(ret, mid)
                right = mid - 1
            if count > h:
                left = mid + 1
        return ret