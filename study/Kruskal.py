'''
개요: Kruskal Algorithm 구현
설명:
UnionFind를 구현했다면 크루스칼 알고리즘 자체를 구현하는데 어렵지는 않음.
우선 weighted graph가 들어왔다는 가정하에 edge를 기준으로 정렬을 함.
정렬하는 이유는 그리디 알고리즘과 연관되어 가장 적은 코스트 부터 연결해 나가기 위함.
그리고 가장 중요한, 그래프를 합치기 전 cycle 검사를 실시.
두개의 노드간 부모가 만약 같다면 두 노드를 합쳤을때 사이클이 생기기 때문에 이때는 넘어가야 함.
부모노드가 다르다면 합치고 cost를 더해나가면 탐색이 다 끝났을때 최소값으로 나오게 되는 원리.
'''
from Union_Find import UnionFind

class Kruskal:
    def __init__(self, n, weighted_graph):
        self.graph = weighted_graph
        self.len = n

    def kruskal(self):
        uf = UnionFind(self.len)
        res = []
        min_w = 0
        for x, y, weight in sorted(self.graph, key=lambda x: x[2]):
            root1 = uf.find(x)
            root2 = uf.find(y)
            if root1 != root2:
                uf.union(root1, root2)
                res.append((x, y, weight))
                min_w += weight
        return res, min_w

if __name__ == "__main__":
    weighted_graph = [(0,1,5),(0,3,2),(0,4,3),(1,4,1),(3,4,10),(1,2,2),(2,5,3),(4,5,4)]
    k = Kruskal(6, weighted_graph)
    res, m = k.kruskal()
    print(res)  # [(1, 4, 1), (0, 3, 2), (1, 2, 2), (0, 4, 3), (2, 5, 3)]
    print(m)    # 11