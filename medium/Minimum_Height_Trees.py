# Problem Link: https://leetcode.com/problems/minimum-height-trees/

'''
문제 요약: edge와 노드 n의 범위가 주어질때, 가장 짧은 트리의 높이를 가진 노드들을 반환하는 문제.
ask: n = 4, edges = [[1,0],[1,2],[1,3]]
answer: [1] (노드가 1일땐 높이 2, 나머진 높이가 3)

해석:
문제를 봤을떄 바로 떠오르는건 높이를 DFS탐색으로 구하는 방법. 하지만 모든 노드에대해서 검사해야 하기 때문에 O(n^2)
모든 노드에 대해 높이 자체를 구해야하기 때문에 DFS도중 가지치기도 할수 없는 상황.
트리관련된 개선법을 아무리 생각해봐도 시간을 줄이기 어렵다 생각해서 뭔가 다른방법이 있는것 같음. 따라서 방법론을 보기위해 솔루션을 참조함.
우선 트리로 보지않고 이걸 그래프의 관점에서 본다는건 나도 생각해본 일이지만 더 발전시킬수 없었음.
내가 생각하지 못한 한가지 굉장히 중요한 포인트는 centroid 이론.
centroid이론이란, 어떤 비순환 그래프에서 topology sorting을 하게될때 마지막 가운데에 남는 중앙노드는 하나 혹은 두개라는 것.
짝수개일때 중앙노드는 두개, 홀수개일때는 한개. 세개가 되려면 순환이 생기기 때문에 불가능.
이를기반으로 알고리즘을 구현해보면,
1.그래프를 만들고 위상정렬처럼 indegree 큐를 만듦. (여기선 leaf라 칭함)
2.leaf노드들을 하나씩 제거하면서 새로운 indegree를 위한 큐를 만듦.
3.남은 노드의 개수가 2개 이하가 될때까지 이를 반복.
남은 노드가 정답이 됨.
위상정렬 자체도 아직 익숙치 않아서 구현에 오래걸림. 아무래도 위상정렬을 더 익숙하게 해서 어떤 상황에서도 적용할수있게 훈련해야겠음.
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return range(n)
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        leaf = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaf.append(i)
        centroid = n
        while centroid > 2:
            centroid -= len(leaf)
            new_leaf = []
            while leaf:
                n_leaf = leaf.pop()
                g = graph[n_leaf].pop()
                graph[g].remove(n_leaf)
                if len(graph[g]) == 1:
                    new_leaf.append(g)
            leaf = new_leaf
        return leaf