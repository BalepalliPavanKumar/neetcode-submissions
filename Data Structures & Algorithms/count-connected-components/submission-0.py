class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def bfs(node):
            queue=deque([node])
            visited.add(node)
            while queue:
                current=queue.popleft()
                for neighbour in graph[current]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        components=0
        visited=set()
        for i in range(n):
            if i not in visited:
                bfs(i)
                components+=1
        return components        