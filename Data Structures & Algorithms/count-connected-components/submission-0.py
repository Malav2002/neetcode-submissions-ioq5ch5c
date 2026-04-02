class UnionFind:
    def __init__(self, n:int):
        self.par=[i for i in range(n)]
        self.rank=[1]*n

    def find(self, x):
        while x!=self.par[x]:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x

    def union(self,x1, x2):
        par1, par2=self.find(x1), self.find(x2)
        if par1==par2:
            return False
        if self.rank[par1]>=self.rank[par2]:
            self.par[par2]=par1
            self.rank[par1]+=self.rank[par2]
        else:
            self.par[par1]=par2
            self.rank[par2]+=self.rank[par1]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        res=n
        for i, j in edges:
            if dsu.union(i,j):
                res-=1
        return res