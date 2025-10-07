class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        dry_day = SortedList()
        last_rain = {}
        for i,rain in enumerate(rains):
            if rain == 0:
                dry_day.add(i)
            else:
                ans[i] = -1
                #find the smallest dry_day that greater that the last_rain[rain]
                if rain in last_rain:
                    left = 0
                    right = len(dry_day) - 1
                    choose_idx = -1
                    while left <= right:
                        mid = left + (right - left) // 2
                        if dry_day[mid] > last_rain[rain]:
                            choose_idx = mid
                            right = mid - 1
                        else:
                            left = mid + 1
                    if choose_idx == -1:
                        return []
                    ans[dry_day[choose_idx]] = rain
                    dry_day.discard(dry_day[choose_idx])
                last_rain[rain] = i
        return ans
                    
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        dry_day = SortedList()
        last_rain = {}
        for i,rain in enumerate(rains):
            if rain == 0:
                dry_day.add(i)
            else:
                ans[i] = -1
                #find the smallest dry_day that greater that the last_rain[rain]
                if rain in last_rain:
                    it = dry_day.bisect(last_rain[rain])
                    if it == len(dry_day): 
                        return []
                    ans[dry_day[it]] = rain
                    dry_day.discard(dry_day[it])
                last_rain[rain] = i
        return ans








