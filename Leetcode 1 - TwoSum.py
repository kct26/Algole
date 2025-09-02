class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hash:
                return [hash[temp],i]
            hash[nums[i]] = i
        return []
    