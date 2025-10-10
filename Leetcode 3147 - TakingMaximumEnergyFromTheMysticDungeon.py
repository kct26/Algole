class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range (len(energy) - 1 - k, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)