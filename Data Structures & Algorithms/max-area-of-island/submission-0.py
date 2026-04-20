class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area=0
        rows,cols=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(i,j):
            queue=deque([(i,j)])
            grid[i][j]=0
            area=1
            while queue:
                current_i,current_j=queue.popleft()
                for di,dj in directions:
                    ni,nj=di+current_i,dj+current_j 
                    if 0<=ni<rows and 0<=nj<cols and grid[ni][nj]==1:
                        queue.append((ni,nj))
                        grid[ni][nj]=0
                        area+=1
            return area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    max_area=max(max_area,bfs(i,j))
        return max_area                            