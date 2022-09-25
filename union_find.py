# aka disjointed set
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, a):
        if self.parent[a] == a:
            return a
        
        # path compression
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb: return

        # merge smaller group to larget group
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]

if __name__ == '__main__':
    uf = UnionFind(4)
    
    uf.union(0, 1)
    uf.union(1, 2)

    assert(uf.find(0) == uf.find(1))
    assert(uf.find(0) == uf.find(2))

    assert(uf.find(0) != uf.find(3))
