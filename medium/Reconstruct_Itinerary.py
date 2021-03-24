# Problem Link: https://leetcode.com/problems/reconstruct-itinerary/

'''
문제 요약: 'JFK' 로부터 모든 티켓을 소모하는 비행 경로를 찾는 문제. (답이 여러개일 경우 사전식 정렬이 가장 빠른 답 하나만)
ask: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
answer: ["JFK","MUC","LHR","SFO","SJC"]

해석:
무조건 'JFK'에서 출발하도록 되어있기에 DFS로 간단하게 해결이 가능한 문제.
우선 입력으로 들어오는 tickets를 그래프 형성을 하고 정렬까지 수행.
이미 티켓을 소모한곳은 다시 들리면 안되기 때문에 visited 를 선언해서 구분해줌.
그 외에는 평범한 DFS이며, 성능자체는 뛰어나지 않은걸 보니 다른 최적화 방법이 있는듯.
다음 복습때는 최적화 시키는 것으로.
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t_len = len(tickets)
        ans = []
        visited = set()
        graph = defaultdict(list)
        for t in tickets:
            graph[t[0]].append(t[1])
        for key, val in graph.items():
            val.sort()

        def dfs(cur, path):
            if len(path) == t_len + 1:
                ans.extend(path)
                return True
            for i, adj in enumerate(graph[cur]):
                if (cur, adj, i) not in visited:
                    visited.add((cur, adj, i))
                    if dfs(adj, path + [adj]):
                        return True
                    visited.remove((cur, adj, i))
            return False

        dfs('JFK', ['JFK'])
        return ans
