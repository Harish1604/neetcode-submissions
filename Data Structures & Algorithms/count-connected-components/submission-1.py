class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        
        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        count = 0
        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node)
        
        return count
        