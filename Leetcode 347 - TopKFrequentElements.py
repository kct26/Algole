class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        count = [[] for i in range (len(nums)+1)]
        for num,fre in freq.items():
            count[fre].append(num)
        res = []
        for i in range (len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return []
