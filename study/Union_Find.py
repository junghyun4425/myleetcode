'''
개요: UnionFind 구현
설명:
UnionFind는 두가지 방법으로 구현이 가능. (배열, 트리)
배열로 구현하면 부모노드를 찾을때 최악의 경우 O(n) 시간복잡도를 가짐.
따라서 어떤 경우에도 O(logn)의 시간복잡도를 가지는 트리로 구현.
init()
각 배열의 부모노드를 자기자신으로 하는 root 배열을 생성.
각 트리의 높이를 구할 배열을 생성.
find()
재귀함수와 반복문 두가지 방법으로 구현할 수 있음.
여기서는 간단한 재귀함수를 통해 해결. (반복문도 구현함)
현재노드 n의 부모를 찾는 함수이며 트리로 구현되었기 때문에 최악의 경우 O(logn)의 시간복잡도를 가짐.
union()
x 와 y 에 대한 부모를 찾고 둘을 합치는 함수.
x, y 의 부모가 같다면 추가할 필요없이 리턴.
둘중 더 높은 트리를 찾아서 나머지 트리를 붙이는 작업. 이를통해 find()의 시간복잡도를 줄일 수 있게 됨.
여기서 주의할 점은 x, y 부모의 트리가 같은높이일 수 있으므로 1더한값을 height로 저장해야할 때도 있음을 고려해 설계해야 함.
'''

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n+1))
        self.height = [0] * (n+1)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.height[x] >= self.height[y]:
            self.root[y] = x
            self.height[x] = max(self.height[y] + 1, self.height[x])
        else:
            self.root[x] = y
            self.height[y] = max(self.height[x] + 1, self.height[y])

    def find(self, n):
        # Recursion
        if n == self.root[n]: return n
        return self.find(self.root[n])

        # Iteration
        '''
        r = self.root[n]
        while r != n:
            n = r
            r = self.root[n]
        return r
        '''

    def print(self):
        print(f'Node   = {self.root}')
        print(f'Height = {self.height}')

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(4, 2)
    uf.union(4, 0)
    uf.union(1, 3)
    uf.union(1, 2)
    print(uf.find(3)) # 1
    print(uf.find(5)) # 5
    uf.print()
    # Node   = [4, 1, 4, 1, 1, 5]
    # Height = [0, 2, 0, 0, 1, 0]