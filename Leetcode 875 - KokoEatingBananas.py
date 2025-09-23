class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_time(speed):
            res = 0
            for bananas in piles:
                res += (bananas + speed - 1) // speed
            return res
        left = 1
        right = max (piles)
        while left <= right:
            mid = left + (right - left) // 2
            timeNeed = total_time(mid)
            if timeNeed > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
        

