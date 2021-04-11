# Problem Link: https://leetcode.com/problems/evaluate-division/

'''
문제 요약: 어떤 변수와 둘을 나눈 결과가 입력으로 주어질때, 쿼리에 답할수 있는 값이면 그 값을 반환하고 아니면 -1을 반환하는 문제.
ask:
equations = [["a","b"],["b","c"]],
values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
answer:
[6.00000,0.50000,-1.00000,1.00000,-1.00000]

해석:
나누기의 결과값을 알기 때문에 둘의 관계와 연관되거나 아니면 연결되어 있을때만 계산이 가능함. (그외에는 -1)
따라서 연결해서 값을 찾아갈 수 있도록 그래프를 활용한 문제.
위의 예제에서 a / c 를 결과값으로 가질수 있는 이유는 둘이 연결되어있기 때문. ( (a / b) * (b / c) = a / c )
따라서 그래프를 cost로 묶듯이 나누기의 결과값으로 묶어서 연결시켜줌.
DFS로 모든 쿼리에대해 답을 찾고, 없다면 -1을 저장하도록 함.
생각나는대로 바로바로 코딩했기 때문에 아마 최적화되지 않은 부분이 많을것. 따라서 다음 복습때 최적화 하는것으로.
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        graph = defaultdict(list)
        for idx, node in enumerate(equations):
            graph[node[0]].append((node[1], values[idx]))
            graph[node[1]].append((node[0], 1 / values[idx]))
        def dfs(start, end, res):
            if start == end:
                ans.append(res)
                return True
            for dest, val in graph[start]:
                if dest in visited:
                    continue
                visited.add(dest)
                if dfs(dest, end, res * val):
                    return True
                visited.remove(dest)
            return False
        for x, y in queries:
            visited = {x}
            if (x not in graph or y not in graph) or not dfs(x, y, 1):
                ans.append(-1.0)
        return ans