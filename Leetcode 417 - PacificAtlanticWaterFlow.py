class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_adj = deque()
        pacific_seen = set()

        atlantic_adj = deque()
        atlantic_seen = set()

        r,c = len(heights), len(heights[0])

        for i in range (c):
            pacific_adj.append((0,i))
            pacific_seen.add((0,i))
        for j in range (1,r):
            pacific_adj.append((j,0))
            pacific_seen.add((j,0))
        for i in range (r-1):
            atlantic_adj.append((i,c-1))
            atlantic_seen.add((i,c-1))
        for j in range (c):
            atlantic_adj.append((r-1,j))
            atlantic_seen.add((r-1,j))
        
        def flow_to_ocean(que, seen):
            while que:
                i,j = que.popleft()
                for i_dir,j_dir in [(-1,0),(1,0),(0,-1),(0,1)]: 
                    current_i, current_j = i + i_dir, j + j_dir
                    if 0 <= current_i < r and 0 <= current_j < c and heights[current_i][current_j] >=  heights[i][j] and (current_i, current_j) not in seen:
                        que.append((current_i,current_j))
                        seen.add((current_i,current_j))
            return seen
        checkPacific = flow_to_ocean(pacific_adj, pacific_seen)
        checkAtlantic = flow_to_ocean(atlantic_adj, atlantic_seen)
        return list(checkPacific.intersection(checkAtlantic))

                

