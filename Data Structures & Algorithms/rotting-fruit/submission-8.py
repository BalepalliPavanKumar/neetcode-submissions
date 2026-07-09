class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=([(1,0),(-1,0),(0,1),(0,-1)])
        queue=deque()
        fresh=0
        time=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
        if not fresh:
            return 0
        if not queue:
            return -1
        while queue:
            current_i,current_j,time=queue.popleft()
            for di,dj in directions:
                ni,nj=current_i+di,current_j+dj
                if 0<=ni<rows and 0<=nj<cols and grid[ni][nj]==1:
                    queue.append((ni,nj,time+1))
                    grid[ni][nj]=2
                    fresh-=1

        return time if fresh==0 else -1                                    