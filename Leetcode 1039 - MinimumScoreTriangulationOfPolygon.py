class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            ans = float('inf')
            for k in range (i + 1, j):
                ans = min(ans, values[i] * values[j] * values[k] + dp(i,k) + dp(k,j))
            return ans
        return dp(0,len(values) - 1)