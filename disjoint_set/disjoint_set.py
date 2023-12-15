class DisjointSet:
    def __init__(self, n: int):
        self.parent = [n for n in range(n)]
        self.ancestor = [n for n in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.ancestor[x] != x:
            self.ancestor[x] = self.find(self.ancestor[x])
        return self.ancestor[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.ancestor[x] = y
        else:
            self.parent[y] = x
            self.ancestor[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


