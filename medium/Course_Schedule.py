# Problem Link: https://leetcode.com/problems/course-schedule/

'''
문제 요약: 특정 수업을 듣기위해서 선수과목을 들어야함. [a,b]일때 b가 선수과목. 수업을 들을수있는지 찾는 문제 (사이클 발견 문제)
ask: numCourses = 2, prerequisites = [[1,0],[0,1]]
answer: False (Cycle. 어떤 코스라도 수강 불가능 상태)

해석:
그래프 문제를 안풀어보다가 풀려니 굉장히 어려웠던 문제. 일단 풀이방법은 상태를 3가지로 나눠서 생각해 해결.
visited의 상태는 총 3가지.
-1 : 아직 아무도 방문하지 않은 상태.
0  : 방문중인 상태. 아직 완료되지 않았고 DFS로 계속 진행중.
1  : 완료된상태. 더이상 방문할곳이 없거나, backtracking으로 올라가면서 완성으로 바꾸는 과정.
여기서 중요한건, DFS로 진행하면서 방문한 노드를 0으로 다 바꿔주고 진행. 이때 0에서 1의 상태를 가진 노드방문은 문제없음. (양쪽에서 하나를 가리키는 경우)
하지만 0에서 0의 상태가진 노드로 방문하는것은 사이클을 의미. 따라서 이런경우 절대 수업을 들을수 없으므로 False.
이 조건만 피하고 모두 수행이 가능하다면 True를 반환.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for e in prerequisites:
            g[e[0]].append(e[1])
        visited = [-1] * numCourses
        def dfs(course):
            if visited[course] == 1:
                return True
            visited[course] = 0
            for i in g[course]:
                if visited[i] == 0 or not dfs(i):
                    return False
            visited[course] = 1
            return True
        for i in range(numCourses):
            if visited[i] == -1 and not dfs(i):
                return False
        return True