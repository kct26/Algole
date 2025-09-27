class TimeMap:

    def __init__(self):
        self.storage = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.storage[key]) - 1
        idx = -1
        while left <= right:
            mid = left + (right - left) // 2
            val = self.storage[key][mid][0]
            if val > timestamp:
                right = mid - 1
            elif val <= timestamp:
                idx = mid
                left = mid + 1
        if idx != -1:
            return self.storage[key][idx][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)