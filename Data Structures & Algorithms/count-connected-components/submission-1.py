class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par=[i for i in range(n)]
        rank =[1]*n

        def find(x):
            while x!=par[x]:
                par[x]=par[par[x]]
                x=par[x]
            return x
        def union(x1,x2):
            p1,p2=find(x1), find(x2)
            if p1==p2:
                return False
            if rank[p1]>=rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        count=n
        for i,j in edges:
            if union(i,j):
                count-=1
        return count