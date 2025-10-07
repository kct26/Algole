import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], (0,0))]
        seen = set()
        while pq:
            x, y = heapq.heappop(pq)
            if y[0] == n - 1 and y[1] == n - 1:
                return x
            if y in seen:
                continue
            seen.add(y)
            for dir in [(-1,0), (1,0), (0, -1), (0, 1)]:
                cur_x = y[0] + dir[0]
                cur_y = y[1] + dir[1]
                if 0 <= cur_x < n and 0 <= cur_y < n:
                    new_d = max (x, grid[cur_x][cur_y])
                    heapq.heappush(pq, (new_d, (cur_x, cur_y)))
        return -1 



