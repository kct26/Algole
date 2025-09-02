class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            temp = numbers[left] + numbers[right]
            if target > temp:
                left +=1 
            elif target < temp:
                right -= 1
            else:
                return [left+1,right+1]
        return