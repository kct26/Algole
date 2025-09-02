class Solution:
    def isPalindrome(self, s: str) -> bool:
        modS = ""
        for char in s:
            if char.isalnum():
                modS += char
        modS = modS.lower()
        left = 0
        right = len(modS)-1
        while left < right:
            if modS[left] != modS[right]:
                return False
            left +=1
            right -=1
        return True