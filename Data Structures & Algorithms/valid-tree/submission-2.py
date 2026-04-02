class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  
            return False

        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for nei in adj[i]:
                if nei==prev:
                    continue
                if not dfs(nei, i):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n