class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs (idx, current):
            if idx == len(nums):
                ans.append(current.copy())
                return
            current.append(nums[idx])
            dfs (idx + 1, current)
            current.pop()
            dfs (idx + 1, current)
        dfs (0, [])
        return ans