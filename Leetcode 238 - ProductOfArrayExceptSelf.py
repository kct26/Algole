class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f = [1]*n
        for i in range(1,n):
            f[i] = f[i-1]*nums[i-1]
        right = 1
        for i in range(n-1,-1,-1):
            f[i] *= right
            right *= nums[i]
        return f
        