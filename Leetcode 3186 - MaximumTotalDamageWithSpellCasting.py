class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        a = {}
        for p in power:
            a[p] = a.get(p, 0) + 1
        vec = []
        for key in sorted(a.keys()):
            vec.append((key, a[key]))
        j = 0
        max_temp = 0
        dp = [0] * len(power)
        for i in range (len(vec)):
            while j < i and vec[j][0] < vec[i][0] - 2:
                max_temp = max(max_temp, dp[j])
                j+=1
            dp[i] = max_temp + vec[i][0] * vec[i][1]
        return max(dp)

