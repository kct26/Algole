class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            if count not in hash:
                hash[count] = []
            hash[count].append(s)
        return list(hash.values())