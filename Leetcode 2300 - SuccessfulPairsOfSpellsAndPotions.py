class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for spell in spells:
            left = 0
            right = len(potions) - 1
            minimum_need = math.ceil(success/spell)
            idx = len(potions)
            while left <= right:
                mid = left + (right - left) // 2
                if potions[mid] >= minimum_need:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            res = len(potions) - idx
            ans.append(res)
        return ans
    