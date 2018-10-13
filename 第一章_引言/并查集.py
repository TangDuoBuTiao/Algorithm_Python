class UnionFind:
    def __init__(self, n):
        print("初始化并查集：")
        self.up = list(range(n))
        self.rank = [0] * n      # 和根元素直接相连接子树的个数

    def find(self, x):  # 查找x的上一级
        if self.up[x] == x:  # 如果x的上级是自己，就返回本身（即x是一个孤立点）
            return x
        else:
            self.up[x] = self.find(self.up[x])  # 一直委托上级找根节点
            return self.up[x]

    def union(self, x, y):
        print(f"合并{x}和{y}后：")
        repr_x = self.find(x)
        repr_y = self.find(y)

        if repr_x == repr_y:  # x和y在同一个连通集合中（有共同的上级）
            return False
        if self.rank[repr_x] == self.rank[repr_y]:  # repr_x所代表的集合和repr_y所代表的集合个数相等
            self.rank[repr_x] += 1
            self.up[repr_y] = repr_x  # 就把repr_y挂在repr_x上
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up[repr_y] = repr_x
        else:
            self.up[repr_x] = repr_y
        return True

    def status(self):
        print(f"up   {self.up}")
        print(f"rank {self.rank}")
        print("------------------------")


uf = UnionFind(6)
uf.status()
uf.union(1, 2)
uf.status()
uf.union(3, 4)
uf.status()
print(uf.find(4))
print(uf.find(2))
uf.union(1,3)
uf.status()